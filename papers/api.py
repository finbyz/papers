import frappe, erpnext
from frappe.utils import flt
import json

@frappe.whitelist()
def insert_item_details(doc_details, item_details):
    from six import string_types

    if isinstance(doc_details, string_types):
        doc_details = json.loads(doc_details)

    doc = frappe.get_doc(doc_details)
    
    item_details = frappe._dict(json.loads(item_details))
    item_details.pop('name')
    item_details.pop('idx')

    to_remove = []
    for row in doc.items:
        if row.item_code == item_details.item_code:
            to_remove.append(row)

    [doc.remove(row) for row in to_remove]

    for row in doc.get('paper_roll_detail'):
        detail = item_details.copy()
        detail.qty = row.qty
        detail.received_qty = row.qty
        detail.stock_qty = row.qty
        detail.amount = flt(row.qty * detail.rate) * doc.conversion_rate
        detail.base_amount = flt(row.qty * detail.rate)
        detail.base_net_amount = flt(row.qty * detail.rate)
        detail.net_amount = flt(row.qty * detail.rate) * doc.conversion_rate
        detail.roll_no = row.roll_no
        
        doc.append('items', detail)


    for idx, row in enumerate(doc.get('items')):
        row.idx = idx + 1

    doc.set('paper_roll_detail', [])

    if doc.is_new():
        doc.insert()
    else:
        doc.save()

    return doc.as_dict()


def conversion_factor_on_save(self,method):
   for row in self.items:
     if row.reverse_conversion_factor:
        row.conversion_factor= 1/row.reverse_conversion_factor
   
def set_qty_on_save(self,method): 
   for row in self.items:
        if row.uom == "Kgs":
            if row.conversion_factor :
                qty = row.stock_qty/row.conversion_factor
                row.qty =qty

def UOM_validation(self,method):
    for row in self.items:
        if row.stock_uom == row.uom:
            if not row.conversion_factor == 1:
                frappe.throw("Stock UOM and UOM are same then conversion_factor should be 1 ")
        if row.stock_uom != row.uom:
            if row.conversion_factor == 1:
                frappe.throw(" Stock UOM and UOM are diffrent then conversion_factor should  Not be 1 ")

def rate_set_on_save(self,method):
    for row in self.items:
        if row.uom == "Kgs":
            rate=row.stock_qty*row.stock_uom_rate/row.qty
            row.rate = rate