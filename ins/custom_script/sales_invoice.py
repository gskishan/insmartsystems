from frappe import utils
import re
import frappe

@frappe.whitelist()
def update_oldrecord():
    sql="""SELECT 
  name,
    company,
    YEAR(posting_date) AS invoice_year,
    ROW_NUMBER() OVER (PARTITION BY company, YEAR(posting_date) ORDER BY creation) AS order_number
FROM 
    `tabSales Invoice`
ORDER BY 
    company, creation;"""
    for d in frappe.db.sql(sql,as_dict=True):
        si=frappe.get_doc("Sales Invoice",d.name)
        si.db_set("sequence",0)

def get_year(posting_date):
    import datetime
    date_string = str(posting_date)
    date_object = datetime.datetime.strptime(date_string, '%Y-%m-%d')
    year = date_object.year
    return year

def validate(self, method=None):
    if self.is_new() and 'param' in self.naming_series:
        try:
            sql = """SELECT MAX(sequence) sequence
                    FROM `tabSales Invoice`
                    WHERE company=%s AND sequence IS NOT NULL and  YEAR(creation) =%s
                    ORDER BY creation DESC
                    LIMIT 1""".format(self.doctype)
            last_count = frappe.db.sql(sql, (self.company,get_year(self.posting_date)), as_dict=False)
            last_count = last_count[0][0] if last_count else None
            if last_count is not None:
                self.sequence = last_count + 1
            else:
                self.sequence = 1	
        except Exception as e:
            frappe.log_error(f"Error setting  sequence: {str(e)}")
    if self.is_new() and 'param' not in self.naming_series:
        self.sequence = 0

    

def autoname(doc, method=None):
    set_name(doc)

import re
import frappe
from frappe.utils import today

def set_name(doc):
    if 'param' in doc.naming_series:
        year = frappe.defaults.get_global_default('fiscal_year')
        month = re.findall(r'\d+', today())[1]
        vertical = doc.vertical
        type = doc.type
        company_code = ""

        if doc.company == "insmart Systems":
            company_code = "10000"
        elif doc.company == "insmart Systems India Private Limited":
            company_code = "20000"
        elif doc.company == "Insmart Systems and Automation Private Limited":
            company_code = "30000"

        sql = """SELECT MAX(sequence)
                    FROM `tab{0}`
                    WHERE company=%s AND sequence IS NOT NULL""".format(doc.doctype)
        max_icv = frappe.db.sql(sql, (doc.company,), as_dict=False)[0][0]

        if max_icv is not None:
            sequence = max_icv + 1
        else:
            sequence = 1

        last_number = f"{int(company_code) + sequence:05d}" 

        doc.name = year + type + month + vertical + last_number


