# Copyright (c) 2024, Patel Asif Khan and contributors
# For license information, please see license.txt

import frappe
from frappe import _


def execute(filters=None):
	columns = get_columns(filters)
	data = get_data(filters)

	return columns, data



def get_columns(filters= None):
	return [
		{
			"label": _("Customer"),
			"fieldname": "customer",
			"fieldtype": "Data",
			"width": 130,
		},
		{
			"label": _("Place"),
			"fieldname": "place",
			"fieldtype": "Data",
			"width": 70,
		},
		{
			"label": _("Vertical"),
			"fieldname": "vertical",
			"fieldtype": "Data",
			"width": 80,
		},
		{
			"label": _("Lead ID"),
			"fieldname": "lead_id",
			"fieldtype": "Link",
			"options": "Lead",
			"width": 200,
		},
		{
			"label": _("Enquiry ID"),
			"fieldname": "enquiry_id",
			"fieldtype": "Link",
			"options": "Enquiry",
			"width": 200,
		},
		{
			"label": _("Quotation ID"),
			"fieldname": "quotation_id",
			"fieldtype": "Link",
			"options": "Quotation",
			"width": 200,
		},
		{
			"label": _("Item Code"),
			"fieldname": "item_code",
			"fieldtype": "Data",
			"width": 100,
		},
		{
			"label": _("Item Name"),
			"fieldname": "item",
			"fieldtype": "Data",
			"width": 120,
		},
		{
			"label": _("Item Group"),
			"fieldname": "item_group",
			"fieldtype": "Data",
			"width": 120,
		},
		{
			"label": _("Qty"),
			"fieldname": "qty",
			"fieldtype": "Data",
			"width": 70,
		},
		{
			"label": _("Rate"),
			"fieldname": "rate",
			"fieldtype": "Data",
			"width": 80,
		},
		{
			"label": _("Amount"),
			"fieldname": "amount",
			"fieldtype": "Currency",
			"width": 80,
		},
		{
            "label": _("Probability"),
            "fieldname": "probability",
            "fieldtype": "Data",
            "width": 100,
        },
		{
			"label": _("Expected Order Date"),
			"fieldname": "expected_order_date",
			"fieldtype": "Data",
			"width": 200,
		},
		{
			"label": _("Status"),
			"fieldname": "status",
			"fieldtype": "Data",
			"width": 100,
		}
	]


def get_data(filters= None):

	customer = filters.customer
	from_date = filters.from_date
	to_date = filters.to_date
	
	result = []
	
	resultant_leads = get_leads(customer,from_date, to_date)
	resultant_enquiry = get_enquiry()
	resultant_quotation = get_quotations()
	
	total_amount = 0
	# Loop All Leads if it matches then update the row
	for each_lead in resultant_leads:
		row = {
				'customer': customer, 
				'place': '', 
				'vertical': '', 
				'lead_id': '', 
				'enquiry_id': '', 
				'quotation_id': '', 
				'item_code': '', 
				'item': '', 
				'item_group': '', 
				'qty': 0, 
				'rate': 0, 
				'amount': 0,
				'probability': '', 
				'link_lead': '',
				'link_enquiry': '',
				'expected_order_date':'',
				'status': ''
			}
		
		row.update(each_lead)
		
		# Check for Linked Enquiry if it matches then update the row
		for each_enquiry in resultant_enquiry:

			if each_lead["lead_id"] == each_enquiry['link_lead'] and each_enquiry["item_code"] == each_lead["item_code"]:
				row.update(each_enquiry)
				
				# Check for Linked Quotation if it matches then update the row
				for each_quotation in resultant_quotation:
					if each_enquiry["enquiry_id"] == each_quotation["link_enquiry"] and each_enquiry["item_code"] == each_quotation["item_code"]:
						row.update(each_quotation)

		result.append(row)
		total_amount += row["amount"]
	result.append({
			'customer': "Total Amount", 
			'amount': total_amount
		})
	return result



def get_leads(customer, from_date, to_date):

	filters={}
	if customer:
		filters['og_name'] = customer
	if from_date and to_date:
		filters["enquiry_date"] = ["between", [from_date, to_date]]

	# Get Lead
	leads = frappe.db.get_all('Lead',
		filters=filters,
		fields=['name', 'og_name'],
	)

	result = []
	for each in leads:
		each_lead = frappe.get_doc("Lead", each.name)
		
		for each_item in each_lead.items: 
			row={}
			row["customer"] =  each.og_name 
			row["lead_id"] =  each.name 
			row["item_code"] = each_item.item_code 
			row["item"] = each_item.item_name 
			row["item_group"] = each_item.item_group 
			row["qty"] = each_item.qty 
			row["rate"] = each_item.rate 
			row["amount"] = each_item.amount
			row["expected_order_date"] = each_lead.expected_order_date 
			row["probability"] = each_lead.probability 
			row["place"] = each_lead.place 
			row["status"] = each_lead.status 
			row["vertical"] = each_lead.vertical 

			result.append(row)

	return result



def get_enquiry():

	# Get Enquiry
	enquiry = frappe.db.get_all('Enquiry',
		fields=['name','customer'],
	)

	result = []
	for each in enquiry:
		each_enq= frappe.get_doc("Enquiry", each.name)
		for each_item in each_enq.items:
			row = {}
			row["customer"] =  each.customer 
			row["enquiry_id"] = each.name
			row["item_code"] = each_item.item_code 
			row["item"] = each_item.item_name
			row["item_group"] = each_item.item_group
			row["qty"] = each_item.qty
			row["rate"] = each_item.rate
			row["amount"] = each_item.amount
			row["link_lead"] = each_enq.lead 
			row["status"] = each_enq.enquiry_status 
			row["expected_order_date"] = each_enq.expected_order_date 
			row["probability"] = each_enq.probability 
			
			result.append(row)


	return result




def get_quotations():

	# Get Quotation
	quotations = frappe.db.get_all('Quotation',
		filters=filters,
		fields=['name','party_name'],
	)

	result = []
	for each in quotations:
		each_quotation = frappe.get_doc("Quotation", each.name)
		for item in each_quotation.items:
			row = {}
			row["customer"] =  each.party_name 
			row["quotation_id"] = each.name
			row["item_code"] = item.item_code
			row["item"] = item.item_name
			row["item_group"] = item.item_group # Need to add this Field fetch it from Item
			row["qty"] = item.qty
			row["rate"] = item.rate
			row["amount"] = item.amount
			row["link_enquiry"] = each_quotation.enquiry 
			row["status"] = each_quotation.status 
			row["expected_order_date"] = each_quotation.valid_till 
			row["probability"] = each_quotation.probability 

			result.append(row)

	return result
