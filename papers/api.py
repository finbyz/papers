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



import frappe
from frappe.utils import (
	add_days,
	add_months,
	cint,
	date_diff,
	flt,
	get_first_day,
	get_last_day,
	get_link_to_form,
	getdate,
	rounded,
	today,
)


import datetime
def before_naming(self , method):
    data = frappe.db.get_value(self.reference_doctype, self.reference_name, "posting_date")
    try:
        self.posting_date = datetime.datetime.strptime(data, "%Y-%m-%d").strftime("%y%m%d")
    except:
        self.posting_date = data.strftime("%y%m%d")



