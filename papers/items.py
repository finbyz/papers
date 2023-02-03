import frappe
from frappe import _
from frappe.utils import nowdate, flt, cint, cstr,now_datetime,getdate, add_days, add_months, get_last_day , get_fullname , get_url_to_form , today

def validation(self,method):
    gsm_1 = frappe.db.get_value("Item Variant Attribute",{'parent':self.name,'attribute':'GSM-1'},'attribute_value') 
    size_w = frappe.db.get_value("Item Variant Attribute",{'parent':self.name,'attribute':'SIZE - W'},'attribute_value')
    size_l = frappe.db.get_value("Item Variant Attribute",{'parent':self.name,'attribute':'Size - L'},'attribute_value')
    sheet_1 = frappe.db.get_value("Item Variant Attribute",{'parent':self.name,'attribute':'Sheet 1'},'attribute_value')
    flag=0
    cf=1.00
    cf = cf * 0.002 / 20000
    if(gsm_1):
        cf = cf*flt(gsm_1)
    if(size_w):
        cf*=flt(size_w)
    if(size_l):
        cf*= flt(size_l)
    if(sheet_1):
        cf*= flt(sheet_1)
    # frappe.msgprint(str(cf))
    for row in self.uoms:
        if(row.uom=='Kgs'):
            row.conversion_factor = cf
            flag=1
    if(flag == 0):
        self.append("uoms",{
            'uom':'Kgs',
            'conversion_factor':cf,
        })
    frappe.msgprint(str(flag))