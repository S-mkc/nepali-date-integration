frappe.provide('frappe.listview_settings');

const DatePickerConfig = {
    CALENDAR_FIELDS: ['nepali_date', 'from_nepali_date', 'to_nepali_date', 'nepali_start_date', 'nepali_end_date',
        'valid_from_bs', 'valid_to_bs', 'warranty_expiry_date_bs', 'expiry_date_bs', 'manufacturing_date_bs',
        'report_date_bs_quality_inspection', 'work_from_date_bs', 'work_end_date_bs', 'from_date_bs', 'to_date_bs',
        'start_date_bs', 'end_date_bs', 'att_fr_date_bs', 'att_to_date_bs', 'effective_from_bs', 'effective_to_bs'],
    initializePickers: function(listview) {
        this.listview = listview;
        this.initializeAllDatePickers();
        this.setupEventListeners(listview);
    },
    initializeAllDatePickers: function() {
        this.CALENDAR_FIELDS.forEach(fieldName => {
            setTimeout(() => this.initDatePicker(fieldName), 100);
        });
    },
    initDatePicker: function(fieldName) {
        $('input[data-fieldname="' + fieldName + '"]').each((_, element) => {
            const $input = $(element);
            if (!$input.hasClass('nepali-picker-initialized')) {
                this.setupDatePickerInput($input, fieldName);
            }
        });
    },
    setupDatePickerInput: function($input, fieldName) {
        if (!$input.parent().hasClass('date-picker-wrapper')) {
            $input.wrap('<div class="date-picker-wrapper"></div>');
        }

        $input.addClass('nepali-picker-initialized')
            .nepaliDatePicker({
                ndpYear: true,
                ndpMonth: true,
                ndpYearCount: 10,
                ndpFormat: 'YYYY-MM-DD',
                onChange: (e) => {
                    const nepaliDate = e.bs;
                    $input.val(nepaliDate);
                    $input.trigger('change');
                }
            });

        this.addCalendarIcon($input);
    },
    addCalendarIcon: function($input) {
        const $parent = $input.parent('.date-picker-wrapper');
        if (!$parent.find('.nepali-calendar-icon').length) {
            const $icon = $('<i>')
                .addClass('fa fa-calendar nepali-calendar-icon')
                .css({
                    'position': 'absolute',
                    'right': '10px',
                    'top': '50%',
                    'transform': 'translateY(-50%)',
                    'cursor': 'pointer',
                    'z-index': '1'
                })
                .on('click', (e) => {
                    e.stopPropagation();
                    $input.focus().trigger('click');
                    if ($input.data('nepaliDatePicker')) {
                        $input.data('nepaliDatePicker').show();
                    }
                });

            $parent.append($icon);
            $input.css('padding-right', '30px');
        }
    },
    setupEventListeners: function(listview) {
        listview.page.wrapper.on('click', '.filter-button', () => {
            setTimeout(() => this.initializeAllDatePickers(), 100);
        });

        const observer = new MutationObserver(() => this.initializeAllDatePickers());
        observer.observe(document.body, { childList: true, subtree: true });

        $(document).on('click', '.filter-list, .filter-box, .filter-button', () => {
            setTimeout(() => this.initializeAllDatePickers(), 100);
        });

        $(document).on('shown.bs.dropdown', '.filter-box', () => {
            setTimeout(() => this.initializeAllDatePickers(), 100);
        });
    }
};

function initializeDatePickersForListView(doctype) {
    frappe.listview_settings[doctype] = {
        onload: function(listview) {
            DatePickerConfig.initializePickers(listview);
        }
    };

    $(document).ready(function() {
        setTimeout(() => {
            if (cur_list && cur_list.doctype === doctype) {
                if (cur_list.filter_area) {
                    cur_list.filter_area.clear();
                }
                DatePickerConfig.initializePickers(cur_list);
            }
        }, 1000);
    });
}

const doctypes = ['Purchase Invoice', 'GL Entry', 'Sales Invoice', 'Journal Entry', 'POS Invoice', 'Employee Attendance Tool'];
doctypes.forEach(doctype => initializeDatePickersForListView(doctype));
