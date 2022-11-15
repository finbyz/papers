from __future__ import unicode_literals

import copy
import json

import frappe
from frappe import _
from frappe.utils import cstr, flt
from six import string_types
import frappe
from frappe.utils import cstr

def make_variant_item_code_with_variant_name(template_item_code, template_item_name, variant):
	"""Uses template's item code and abbreviations to make variant's item code"""
	if variant.item_code:
		return
	attrbt=[]
	abbreviations = []
	for attr in variant.attributes:
		item_attribute = frappe.db.sql("""select i.numeric_values, v.abbr,v.attribute_value, i.attribute_suffix
			from `tabItem Attribute` i left join `tabItem Attribute Value` v
				on (i.name=v.parent)
			where i.name=%(attribute)s and (v.attribute_value=%(attribute_value)s or i.numeric_values = 1)""", {
				"attribute": attr.attribute,
				"attribute_value": attr.attribute_value
			}, as_dict=True)
		
		attrbt.append(attr.attribute_value)

		if not item_attribute:
			continue
			# frappe.throw(_('Invalid attribute {0} {1}').format(frappe.bold(attr.attribute),
			# 	frappe.bold(attr.attribute_value)), title=_('Invalid Attribute'),
			# 	exc=InvalidItemAttributeValueError)

		abbr_or_value = cstr(attr.attribute_value) if (item_attribute[0].numeric_values and attr.attribute_value > 0) else item_attribute[0].abbr
		attribute_name = cstr(attr.attribute_value)
		attribute_suffix = cstr(item_attribute[0].attribute_suffix) or ''
		abbreviations.append({'abbr_or_value':abbr_or_value,'attribute_name':attribute_name, 'attribute_suffix': attribute_suffix})
	if abbreviations:
		item_code_suffix=[]

		for e in abbreviations:
			if e.get('attribute_suffix'):
				e['attribute_suffix'] = " " + e['attribute_suffix']

			if e.get('abbr_or_value'):
				item_code_suffix.append(e.get('abbr_or_value')+e.get('attribute_suffix'))
		
		variant.item_code = "{0}-{1}".format(template_item_name," ".join(item_code_suffix))
		variant.item_name = "{0}-{1}".format(template_item_name," ".join(item_code_suffix))


def copy_attributes_to_variant(item, variant):
	# copy non no-copy fields

	exclude_fields = ["naming_series", "item_code", "item_name", "published_in_website",
		"opening_stock", "variant_of", "valuation_rate", "has_variants", "attributes"]

	if item.variant_based_on=='Manufacturer':
		# don't copy manufacturer values if based on part no
		exclude_fields += ['manufacturer', 'manufacturer_part_no']

	allow_fields = [d.field_name for d in frappe.get_all("Variant Field", fields = ['field_name'])]
	if "variant_based_on" not in allow_fields:
		allow_fields.append("variant_based_on")
	for field in item.meta.fields:
		# "Table" is part of `no_value_field` but we shouldn't ignore tables
		if (field.reqd or field.fieldname in allow_fields) and field.fieldname not in exclude_fields:
			if variant.get(field.fieldname) != item.get(field.fieldname):
				if field.fieldtype == "Table":
					variant.set(field.fieldname, [])
					for d in item.get(field.fieldname):
						row = copy.deepcopy(d)
						if row.get("name"):
							row.name = None
						variant.append(field.fieldname, row)
				else:
					variant.set(field.fieldname, item.get(field.fieldname))

	variant.variant_of = item.name

	if 'description' not in allow_fields:
		if not variant.description:
				variant.description = ""
	else:
		if item.variant_based_on=='Item Attribute':
			if variant.attributes:
				attributes_description = item.description + " "
				# for d in variant.attributes:
				# 	attributes_description += "<div>" + d.attribute + ": " + cstr(d.attribute_value) + "</div>"
				if attributes_description not in variant.description:
					variant.description = attributes_description

def update_variants(variants, template, publish_progress=True):
	total = len(variants)
	for count, d in enumerate(variants, start=1):
		variant = frappe.get_doc("Item", d)
		copy_attributes_to_variant(template, variant)
		variant.save()
		if publish_progress:
			frappe.publish_progress(count / total * 100, title=_("Updating Variants..."))

def update_variants_enqueue(self):
	if self.flags.dont_update_variants or \
					frappe.db.get_single_value('Item Variant Settings', 'do_not_update_variants'):
		return
	if self.has_variants:
		variants = frappe.db.get_all("Item", fields=["item_code"], filters={"variant_of": self.name})
		if variants:
			if len(variants) <= 30:
				update_variants(variants, self, publish_progress=False)
				frappe.msgprint(_("Item Variants updated"))
			else:
				frappe.enqueue("papers.item_variant_overrides.update_variants",
					variants=variants, template=self, now=frappe.flags.in_test, timeout=600)

def validate_is_incremental(numeric_attribute, attribute, value, item):
	from_range = numeric_attribute.from_range
	to_range = numeric_attribute.to_range
	increment = numeric_attribute.increment

	if increment == 0:
		# defensive validation to prevent ZeroDivisionError
		frappe.throw(_("Increment for Attribute {0} cannot be 0").format(attribute))

	is_in_range = from_range <= flt(value) <= to_range
	precision = max(len(cstr(v).split(".")[-1].rstrip("0")) for v in (value, increment))
	# avoid precision error by rounding the remainder
	remainder = flt((flt(value) - from_range) % increment, precision)

	is_incremental = remainder == 0 or remainder == increment


	# Finbyz Changes for Decimal Value
	# if not (is_in_range and is_incremental):
	# 	frappe.throw(
	# 		_(
	# 			"Value for Attribute {0} must be within the range of {1} to {2} in the increments of {3} for Item {4}"
	# 		).format(attribute, from_range, to_range, increment, item),
	# 		InvalidItemAttributeValueError,
	# 		title=_("Invalid Attribute"),
	# 	)
	
	if not is_in_range:
		frappe.throw("Value is not beetween given range.")
