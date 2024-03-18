// Copyright (c) 2024, Patel Asif Khan and contributors
// For license information, please see license.txt

frappe.query_reports["Sales Report Prod"] = {
	"filters": [
		{
			fieldname:"customer",
			label: __("Customer"),
			fieldtype: "Link",
			options: "Customer"
		},
		{
			fieldname:"from_date",
			label: __("Start Date"),
			fieldtype: "Date",
			default: frappe.datetime.add_months(frappe.datetime.nowdate(), -1),
		},
		{
			fieldname:"to_date",
			label: __("End Date"),
			fieldtype: "Date",
			default: frappe.datetime.nowdate(),
		}
	]
};
