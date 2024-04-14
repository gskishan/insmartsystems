from frappe import utils
import re
import frappe

def validate(self,method=None):
    if self.is_new():
        try:
            sql = """SELECT sequence
                    FROM `tab{0}`
                    WHERE company=%s AND sequence IS NOT NULL
                    ORDER BY creation DESC
                    LIMIT 1""".format(self.doctype)
        
            last_count = frappe.db.sql(sql, (self.company,), as_dict=False)

            last_count = last_count[0][0] if last_count else None

            if last_count is not None:
                self.sequence = last_count + 1
            else:
                self.sequence = 1	
        except Exception as e:
            frappe.log_error(f"Error setting  count: {str(e)}")

def autoname(doc, method=None):
    set_name(doc)

def set_name(doc):
    old_doc = doc.get_doc_before_save()
    if old_doc is None and 'param' in doc.naming_series:
        st_year = re.findall(r'\d+', frappe.defaults.get_user_default("year_start_date"))[0][-2:]
        ed_year = re.findall(r'\d+', frappe.defaults.get_user_default("year_end_date"))[0][-2:]
        month = re.findall(r'\d+', utils.today())[1]
        vertical = doc.vertical
        type = doc.type

        company_code = ""
        if doc.company == "insmart Systems":
            company_code = "10000"
        elif doc.company == "insmart Systems India Private Limited":
            company_code = "20000"
        elif doc.company == "OIA TECHNOLOGIES PRIVATE LIMITED":
            company_code = '30000'

        sql = """SELECT MAX(sequence)
                    FROM `tab{0}`
                    WHERE company=%s AND sequence IS NOT NULL""".format(doc.doctype)
        max_icv = frappe.db.sql(sql, (doc.company,), as_dict=False)[0][0]
        if max_icv is not None:
            sequence = max_icv + 1
        else:
            sequence = 1
        last_number=int(company_code) + sequence


        
    
        if last_number == 0:
            last_number = int(company_code) + 1

        doc.name = st_year + ed_year + type + month + vertical + str(last_number)

