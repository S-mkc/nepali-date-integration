frappe.ui.form.ControlDatetime = class ControlDatetime extends frappe.ui.form.ControlDate {
    make_input() {
        super.make_input();

        if (this.datepicker) {
            this.datepicker.destroy();
            this.datepicker = null;
        }

        // Clear existing elements
        this.$wrapper.find(".datepicker-icon").remove();
        this.$input.attr("type", "text");

        // Wrap input for better layout
        this.$wrapper.addClass("nepali-datetime-wrapper");

        // Create time input
        this.$time_input = $(`<input type="time" class="form-control">`).appendTo(this.$wrapper);
        this.$time_input.css({ width: '48%', marginLeft: '4%' });

        // Initialize nepali date picker
        this.$input.nepaliDatePicker({
            ndpYear: true,
            ndpMonth: true,
            ndpYearCount: 10,
            ndpFormat: 'YYYY-MM-DD',
            closeOnDateSelect: true,
            onChange: (e) => {
                this.set_combined_datetime();
            }
        });

        // Also trigger on time input change
        this.$time_input.on('change', () => this.set_combined_datetime());

        this.refresh_input();
    }

    set_combined_datetime() {
        const bs_date = this.$input.val();
        let time = this.$time_input.val() || '00:00';

        try {
            const ad_date = NepaliFunctions.BS2AD(bs_date, "YYYY-MM-DD", "YYYY-MM-DD");
            const ad_datetime = `${ad_date} ${time}:00`; // Add seconds
            this.set_model_value(ad_datetime);
        } catch (e) {
            console.error("Failed to convert BS to AD:", bs_date, e);
        }
    }

    set_formatted_input(value) {
        if (!value || typeof value !== 'string') return;

        const [ad_date, time = '00:00:00'] = value.split(" ");
        try {
            const bs_date = NepaliFunctions.AD2BS(ad_date, "YYYY-MM-DD", "YYYY-MM-DD");
            this.$input && this.$input.val(bs_date);
            this.$time_input && this.$time_input.val(time.slice(0, 5));
        } catch (err) {
            this.$input && this.$input.val('');
            this.$time_input && this.$time_input.val('');
        }
    }

    format_for_input(value) {
        if (!value || typeof value !== 'string') return '';

        const [ad_date] = value.split(" ");
        try {
            return NepaliFunctions.AD2BS(ad_date, "YYYY-MM-DD", "YYYY-MM-DD");
        } catch (e) {
            return '';
        }
    }

    parse(value) {
        if (!value) return '';

        const [bs_date, time = '00:00'] = value.split(' ');
        try {
            const ad_date = NepaliFunctions.BS2AD(bs_date, "YYYY-MM-DD", "YYYY-MM-DD");
            return `${ad_date} ${time}:00`;
        } catch (e) {
            return value;
        }
    }
};
