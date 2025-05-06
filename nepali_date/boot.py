import frappe 

def get_boot_info(bootinfo):
    if frappe.session.user != "Guest":
        frappe.clear_cache(user = frappe.session.user)
        user_doc = frappe.get_doc("User", frappe.session.user)
        bootinfo["user"]["use_ad_date"] = user_doc.get("use_ad_date", 0)
    
# nepali_date/utils/boot_patch.py
def boot_patch(bootinfo):
    import frappe
    from nepali_date.date import format_value as custom_format_value

    # Patch at top level
    frappe.format_value = custom_format_value

    # Patch inside frappe.utils.data (used by reports/print)
    try:
        import frappe.utils.data
        frappe.utils.data.format_value = custom_format_value
    except Exception:
        pass

    # Patch Jinja if needed (for reports using Jinja environment)
    try:
        from frappe.utils.jinja import get_jenv
        jenv = get_jenv()
        jenv.globals['format_value'] = custom_format_value
    except Exception:
        pass

    return bootinfo
