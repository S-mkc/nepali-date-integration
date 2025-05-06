frappe.form.formatters.Datetime = function(value, df, options, doc) {
	if (!value) return '';

	try {
		const [ad_date, time = '00:00:00'] = value.split(" ");
		const bs_date = NepaliFunctions.AD2BS(ad_date, "YYYY-MM-DD", "YYYY-MM-DD");
		return `${bs_date} ${time.slice(0, 5)}`; // HH:mm
	} catch (e) {
		console.error("BS format failed, fallback to AD:", value);
		return frappe.datetime.str_to_user(value);
	}
};
