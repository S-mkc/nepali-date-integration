import frappe
from dataclasses import fields
from frappe import _


def create_custom_fields():
    custom_fields = {
        "User": [
            {"fieldname": "use_ad_date", "label": "Use Ad Date", "fieldtype": "Check", "insert_after": "username"},
        ],
        "Purchase Invoice": [
            {"fieldname": "nepali_date", "label": "Nepali Date", "fieldtype": "Data", "insert_after": "posting_date"}
        ]
    }
    created_fields = [] 

    for doctype_name, fields in custom_fields.items():
        for field in fields:
            if not frappe.db.exists("Custom Field", {"dt": doctype_name, "fieldname": field["fieldname"]}):
                custom_field = frappe.get_doc({
                    "doctype": "Custom Field",
                    "dt": doctype_name,
                    "module": "Nepali Date",
                    **field
                })
                custom_field.save()
                frappe.msgprint(_(f"Custom field '{field['label']}' added successfully to {doctype_name}!"))
                created_fields.append({"dt": doctype_name, "fieldname": field["fieldname"]})  # Store created field info
            else:
                frappe.msgprint(_(f"Field '{field['label']}' already exists in {doctype_name}."))

    return created_fields  

create_custom_fields()