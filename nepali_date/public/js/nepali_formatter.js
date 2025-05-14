frappe.form.formatters.Date = function(value, df, options, doc) {
    if (!value) return '';

    if (window.use_ad_date) {
        // Use default formatting (AD)
        return frappe.datetime.str_to_user(value);
    }

    // When user prefers BS date
    try {
        const bs_date = NepaliFunctions.AD2BS(value, "YYYY-MM-DD", "YYYY-MM-DD");
        return bs_date;
    } catch (e) {
        console.error("Date formatting failed (AD to BS)", value, e);
        return frappe.datetime.str_to_user(value);
    }
};
