import frappe
from dataclasses import fields
from frappe import _


def create_custom_fields():
    custom_fields = {
        "User": [
            {"fieldname": "use_ad_date", "label": "Use Ad Date", "fieldtype": "Check", "insert_after": "username", 
            "description": "<b>Disclaimer:</b> Checking this means you prefer using the default date picker (AD format) as your preferred format."},
        ],
        "Purchase Invoice": [
            {"fieldname": "nepali_date", "label": "Nepali Date", "fieldtype": "Data", "insert_after": "posting_date"}
        ],
        "Employee": [
            {"fieldname": "revised_salary", "label": "Revised Salary", "fieldtype": "Currency", "insert_after": "payroll_cost_center", "reqd": 1},
        ],
         "Salary Slip": [
            {"fieldname": "taxable_salary", "label": "Taxable Salary", "fieldtype": "Currency", "insert_after": "total_deduction"},
        ],
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
                created_fields.append({"dt": doctype_name, "fieldname": field["fieldname"]})  
            else:
                frappe.msgprint(_(f"Field '{field['label']}' already exists in {doctype_name}."))

    return created_fields  

create_custom_fields()
