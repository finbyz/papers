import frappe
from frappe.utils import nowdate, get_url_to_form, flt, cstr, getdate, get_fullname, now_datetime, parse_val, add_years, add_days, get_link_to_form

def je_validate(self, method):
	if self.voucher_type == "Journal Entry" and self.bill_no and self.pay_to_recd_from:
		if frappe.db.exists("Journal Entry",{"docstatus":1,"bill_no":self.bill_no,"voucher_type":"Journal Entry","pay_to_recd_from":self.pay_to_recd_from,'fiscal':self.fiscal}):
			entry_no = frappe.db.exists("Journal Entry",{"docstatus":1,"bill_no":self.bill_no,"voucher_type":"Journal Entry","pay_to_recd_from":self.pay_to_recd_from,'fiscal':self.fiscal})
			url = get_url_to_form("Journal Entry", entry_no)
			frappe.throw("Bill No. Should be Unique, Current Bill No: '{}' found in <b><a href='{}'>{}</a></b>".format(frappe.bold(self.bill_no),url,entry_no))