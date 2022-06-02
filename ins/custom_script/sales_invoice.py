from frappe import utils
import re
import frappe


def before_save(doc, method=None):
	set_name(doc)

def set_name(doc):
		series = re.findall(r'\d+',doc.name)[0]
		month=re.findall(r'\d+',utils.today())[1]
		st_year = re.findall(r'\d+',frappe.defaults.get_user_default("year_start_date"))[0][-2::]
		ed_year = re.findall(r'\d+',frappe.defaults.get_user_default("year_end_date"))[0][-2::]
		vertical=doc.vertical
		type = doc.type
		doc.name = st_year+ed_year+type+month+vertical+series
		return doc.name