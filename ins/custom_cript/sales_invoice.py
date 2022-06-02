from frappe import utils
import re
import frappe

def set_custom_name(self):
		series = re.findall(r'\d+',self.name)[0]
		month=re.findall(r'\d+',utils.today())[1]
		st_year = re.findall(r'\d+',frappe.defaults.get_user_default("year_start_date"))[0][-2::]
		ed_year = re.findall(r'\d+',frappe.defaults.get_user_default("year_end_date"))[0][-2::]
		vertical=self.vertical
		type = self.type
		self.name = st_year+ed_year+type+month+vertical+series
		return self.name

