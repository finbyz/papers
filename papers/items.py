import frappe
from frappe import _
from frappe.utils import nowdate, flt, cint, cstr,now_datetime,getdate, add_days, add_months, get_last_day , get_fullname , get_url_to_form , today

def validation(self,method):
    pass
#     gsm_1 = frappe.db.get_value("Item Variant Attribute",{'parent':self.name,'attribute':'GSM-1'},'attribute_value') 
#     size_w = frappe.db.get_value("Item Variant Attribute",{'parent':self.name,'attribute':'SIZE - W'},'attribute_value')
#     size_l = frappe.db.get_value("Item Variant Attribute",{'parent':self.name,'attribute':'Size - L'},'attribute_value')
#     sheet_1 = frappe.db.get_value("Item Variant Attribute",{'parent':self.name,'attribute':'Sheet 1'},'attribute_value')
#     flag=0
#     cf=1.00
#     if not gsm_1:
#         frappe.msgprint("GSM-1 Attribute Is Missing")
#     else:
#         cf = cf*flt(gsm_1)
#     if  not size_w:
#          frappe.msgprint("SIZE - W Attribute Is Missing")
#     else:
#         cf*=flt(size_w)
#     if not size_l:
#          frappe.msgprint("SIZE - L Attribute Is Missing")
#     else:
#               cf*= flt(size_l)
#     cf/=10000000
#     if not sheet_1 :
#         frappe.msgprint("sheet_1 Attribute Is Missing")
#     else:
#         cf*= flt(sheet_1)
#     if gsm_1 and size_w and size_l and sheet_1:
#         for row in self.uoms:
#             if(row.uom=='Kgs'):
#                 row.conversion_factor = 1/cf
#                 flag=1
        # if(flag == 0):
        #     self.append("uoms",{
        #         'uom':'Kgs',
        #         'conversion_factor':1/cf,
        #     })

def patches():
    item_list = frappe.db.get_list("Item" , {'has_variants' : 0} , pluck='name')
    for row in item_list:
        doc = frappe.get_doc("Item" , row)
        for d in doc.attributes:
            if d.attribute == 'Ream Weight':
                frappe.db.set_value("Item" , row , 'weight_per_unit' , d.attribute_value , update_modified = False)
                frappe.db.set_value("Item" , row , 'weight_uom' , 'Kgs' , update_modified = False)
