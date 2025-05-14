import frappe
from hrms.payroll.doctype.salary_slip.salary_slip import SalarySlip

class CustomSalarySlip(SalarySlip):
    def validate_net_pay(self):
        # Allow negative net pay
        pass

    def on_submit(self):
        # Optional: replicate ERPNext default on_submit logic if needed
        self.status = 'Submitted'
        self.set_status()
