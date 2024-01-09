# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors

import frappe
from frappe import _


@frappe.whitelist()
def before_submit(self,method):
	if self.enquiry:
		if frappe.db.exists("Enquiry", self.enquiry):
			enq=frappe.get_doc("Enquiry", self.enquiry)
			enq.db_set("status","Quotation")

@frappe.whitelist()
def on_cancel(self,method):
	if self.enquiry:
		if frappe.db.exists("Enquiry", self.enquiry):
			enq=frappe.get_doc("Enquiry", self.enquiry)
			enq.db_set("status","")
