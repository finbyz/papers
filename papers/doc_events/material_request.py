import frappe
from erpnext.stock.doctype.material_request.material_request import MaterialRequest

class CustomMaterialRequest(MaterialRequest):
	def validate_material_request_type(self):
		"""Validate fields in accordance with selected type"""
        # override for customer value in matreial request it is set in any condition
		pass
	