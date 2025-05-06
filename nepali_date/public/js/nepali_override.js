frappe.after_ajax(() => {
    frappe.call({
        method: "frappe.client.get_value",
        args: {
            doctype: "User",
            filters: { name: frappe.session.user },
            fieldname: "use_ad_date"
        },
        callback: (r) => {
            const use_ad_date = r.message?.use_ad_date;
            window.use_ad_date = use_ad_date; // store globally
            override_with_nepali_date_picker(use_ad_date);
        }
    });
});

function override_with_nepali_date_picker(use_ad_date) {
    // CASE 1: If using AD (default ERPNext date picker)
    if (use_ad_date) {
        const originalSetFormattedInput = frappe.ui.form.ControlDate.prototype.set_formatted_input;

        frappe.ui.form.ControlDate = class ControlDate extends frappe.ui.form.ControlDate {
            set_formatted_input(value) {
                originalSetFormattedInput.call(this, value);

                if (value && typeof value === "string") {
                    try {
                        const bs_date = NepaliFunctions.AD2BS(value, "YYYY-MM-DD", "YYYY-MM-DD");
                        this.show_equivalent_date(`BS Date: ${bs_date}`);
                    } catch (err) {
                        console.error("Failed to convert AD to BS", err);
                    }
                }
            }

            show_equivalent_date(text) {
                const equivalentTextDiv = this.$wrapper.find('.equivalent-date');
                if (!equivalentTextDiv.length) {
                    // If equivalent date does not exist, append it right below the input field without extra margin
                    this.$wrapper.append(`<div class="equivalent-date" style="font-size: 0.9em; color: #888; margin-top: 1px; padding-top: 2px;">${text}</div>`);
                } else {
                    // Otherwise, just update the existing text
                    equivalentTextDiv.text(text);
                }
            }
        };
        return;
    }

    // CASE 2: If using BS (override default date picker with Nepali)
    frappe.ui.form.ControlDate = class ControlDate extends frappe.ui.form.ControlData {
        make_input() {
            super.make_input();

            if (this.datepicker) {
                this.datepicker.destroy();
                this.datepicker = null;
            }

            this.$wrapper.find(".datepicker-icon").remove();
            this.$input.attr("type", "text");

            this.$input.nepaliDatePicker({
                ndpYear: true,
                ndpMonth: true,
                ndpYearCount: 10,
                ndpFormat: 'YYYY-MM-DD',
                closeOnDateSelect: true,
                onChange: (e) => {
                    const bs_date = e.bs;
                    const ad_date = NepaliFunctions.BS2AD(bs_date, "YYYY-MM-DD", "YYYY-MM-DD");

                    this.$input.val(bs_date);
                    this.set_model_value(ad_date);
                    this.show_equivalent_date(`AD Date: ${ad_date}`);
                }
            });

            this.refresh_input();
        }

        show_equivalent_date(text) {
            const equivalentTextDiv = this.$wrapper.find('.equivalent-date');
            if (!equivalentTextDiv.length) {
                // Append equivalent date text with reduced margin
                this.$wrapper.append(`<div class="equivalent-date" style="font-size: 0.9em; color: #888; margin-top: 1px; padding-top: 2px;">${text}</div>`);
            } else {
                equivalentTextDiv.text(text);
            }
        }

        set_formatted_input(value) {
            if (!value || typeof value !== 'string') return;

            try {
                const bs_date = NepaliFunctions.AD2BS(value, "YYYY-MM-DD", "YYYY-MM-DD");
                this.$input && this.$input.val(bs_date);
                this.show_equivalent_date(`AD Date: ${value}`);
            } catch (err) {
                console.error("AD conversion failed", value, err);
            }
        }

        format_for_input(value) {
            if (!value || typeof value !== 'string') return '';
            if (/^\d{4}-\d{2}-\d{2}$/.test(value)) {
                try {
                    return NepaliFunctions.AD2BS(value, "YYYY-MM-DD", "YYYY-MM-DD");
                } catch (e) {
                    console.error("format_for_input failed", value, e);
                }
            }
            return '';
        }

        parse(value) {
            if (value === "Today") {
                const bs_today = NepaliFunctions.getToday();
                return NepaliFunctions.BS2AD(bs_today, "YYYY-MM-DD", "YYYY-MM-DD");
            }

            if (/^20\d{2}-\d{2}-\d{2}$/.test(value)) {
                return NepaliFunctions.BS2AD(value, "YYYY-MM-DD", "YYYY-MM-DD");
            }

            return value || '';
        }
    };
}
