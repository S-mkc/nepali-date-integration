import frappe
from datetime import datetime
import calendar
from frappe import _

def execute(filters=None):
	columns, data = [], []
	nepali_month = filters.get("nepali_month")
	nepali_year = filters.get("nepali_year")

	# If no Nepali month is selected, set month_pattern to match all data
	if not nepali_month:
		# To show all records, use '%' wildcard in LIKE for all months
		month_pattern = "%"
	else:
		# Map Nepali months to number
		nepali_month_map = {
			"Baishakh": "01", "Jestha": "02", "Ashadh": "03", "Shrawan": "04",
			"Bhadra": "05", "Ashwin": "06", "Kartik": "07", "Mangsir": "08",
			"Poush": "09", "Magh": "10", "Falgun": "11", "Chaitra": "12"
		}

		month_number = nepali_month_map.get(nepali_month)
		if not month_number:
			frappe.throw(_("Invalid Nepali Month selected."))
		
		# For the selected Nepali month, format the month_pattern to filter by month
		month_pattern = f"%-{month_number}-%"

	# Initialize conditions variable
	conditions = ""

	if filters.get("from_nepali_date") and filters.get("to_nepali_date"):
		from_nepali_date = filters["from_nepali_date"]
		to_nepali_date = filters["to_nepali_date"]
		conditions += " AND pi.nepali_date BETWEEN %(from_nepali_date)s AND %(to_nepali_date)s"

	if filters.get("supplier"):
		conditions += " AND pi.supplier = %(supplier)s"
	# Define report columns
	columns = [
		_("Invoice Date") + ":Date:150",
		# _("Nepali Date") + ":Data:150",
		_("Supplier") + ":Link/Supplier:150",
		_("Invoice Number") + ":Link/Purchase Invoice:120",
		_("Qty") + ":Float:60",
		_("Amount") + ":Currency:100",
		_("Tax and Charges Added") + ":Currency:120",
		_("Discount") + ":Currency:120",
		_("Total") + ":Currency:120",
		_("Net Total") + ":Currency:120",
		_("Grand Total") + ":Currency:120",
		_("Total Advance") + ":Currency:120",
		_("Outstanding Amount") + ":Currency:120",
		_("Status") + ":Data:80",
	]

	query = """
		SELECT
			pi.posting_date,
			# pi.nepali_date,
			pi.supplier,
			pi.name AS invoice_number,
			SUM(item.qty) AS total_qty,
			SUM(item.qty * item.rate) AS total_amount,
			pi.taxes_and_charges_added AS taxes_and_charges_added,
			pi.discount_amount AS discount_amount,
			pi.total AS total,
			pi.net_total AS net_total,
			pi.grand_total AS grand_total,
			pi.total_advance AS total_advance,
			pi.outstanding_amount AS outstanding_amount,
			pi.status
		FROM
			`tabPurchase Invoice` pi
		JOIN
			`tabPurchase Invoice Item` item ON item.parent = pi.name
		WHERE
			pi.docstatus = 1
			AND pi.nepali_date LIKE %(month_pattern)s
			{conditions}
		GROUP BY
			pi.name
		ORDER BY
			pi.posting_date DESC
	""".format(conditions=conditions)

	values = {
		"month_pattern": month_pattern,
		"from_nepali_date": filters.get("from_nepali_date"),
		"to_nepali_date": filters.get("to_nepali_date"),
		"supplier": filters.get("supplier")
	}

	result = frappe.db.sql(query, values=values, as_dict=True)

	data = [[
		row.posting_date,
		# row.nepali_date,
		row.supplier,
		row.invoice_number,
		row.total_qty,
		row.total_amount,
		row.taxes_and_charges_added,
		row.discount_amount,
		row.total,
		row.net_total,
		row.grand_total,
		row.total_advance,
		row.outstanding_amount,
		row.status
	] for row in result]

	return columns, data

