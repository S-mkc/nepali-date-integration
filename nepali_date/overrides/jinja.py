import frappe
from frappe.utils import getdate, formatdate
from nepali_date.utils.nepali_date import ad_to_bs_string

def inject_bs_formatter():
    frappe.log_error("🚀 Nepali Date: Injecting Jinja Filters")  # Debug log

    def bs_format_date(value, df=None):
        if not value:
            return ""
        try:
            ad_date = getdate(value)
            return ad_to_bs_string(ad_date)
        except Exception as e:
            frappe.log_error(f"[Nepali Date] BS format failed: {e}")
            return formatdate(value)  # fallback

    # Register filter
    frappe.local.jenv.filters["format_date_bs"] = bs_format_date
    frappe.local.jenv.filters["format_date"] = bs_format_date  # Optional: override default
