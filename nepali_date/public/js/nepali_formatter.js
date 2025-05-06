frappe.form.formatters.Date = function(value, df, options, doc) {
    if (!value) return '';

    try {
        const bs_date = NepaliFunctions.AD2BS(value, "YYYY-MM-DD", "YYYY-MM-DD");
        return bs_date;  // 🧠 Display BS in read-only mode
    } catch (e) {
        console.error("BS format failed, fallback to AD:", value);
        return frappe.datetime.str_to_user(value); // fallback to AD
    }
};
