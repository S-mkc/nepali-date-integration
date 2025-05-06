# nepali_date/patch.py

import frappe
from datetime import datetime
from nepali_date.date import custom_format_value

def convert_all_dates_to_bs(doc):
    """
    Recursively convert all datetime.date or date strings in `doc` to Nepali BS format.
    """
    if isinstance(doc, dict):
        return {
            key: convert_all_dates_to_bs(value)
            for key, value in doc.items()
        }
    elif isinstance(doc, list):
        return [convert_all_dates_to_bs(item) for item in doc]
    elif isinstance(doc, str):
        # Check if the string is in a valid date format (YYYY-MM-DD)
        try:
            ad_date = datetime.strptime(doc, "%Y-%m-%d").date()
            # Convert to BS date using your existing logic
            return custom_format_value(ad_date, {"fieldtype": "Date"})
        except ValueError:
            # If the string is not a valid date, return as is
            return doc
    elif isinstance(doc, datetime.date):
        # If it's already a date object, convert to BS
        return custom_format_value(doc, {"fieldtype": "Date"})
    
    return doc  # Return non-date values as they are


def patch_print_context():
    """
    Patch the get_context method to automatically format date fields to Nepali BS.
    """
    import frappe.www.printview
    original_get_context = frappe.www.printview.get_context

    def custom_get_context(context):
        ctx = original_get_context(context)
        if "doc" in ctx:
            ctx["doc"] = convert_all_dates_to_bs(ctx["doc"])
        return ctx

    frappe.www.printview.get_context = custom_get_context
