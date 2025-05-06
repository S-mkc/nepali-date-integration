import frappe
# from .date import NepaliDate 

__version__ = "0.0.1"

# nepali_date/__init__.py

def safe_patch_format_value():
    import frappe
    from frappe import format_value as original_format_value
    from nepali_date.date import format_value
    from nepali_date.date import custom_format_value

    # Patch both references
    frappe.format_value = custom_format_value

    # Also patch modules that might cache it
    try:
        import frappe.utils.data
        frappe.utils.data.format_value = custom_format_value
    except Exception:
        pass

safe_patch_format_value()

