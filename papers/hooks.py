from . import __version__ as app_version

app_name = "papers"
app_title = "Papers"
app_publisher = "Finbyz Tech Pvt Ltd"
app_description = "Custom App for Paper Industries"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "info@finbyz.com"
app_license = "MIT"


# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/papers/css/papers.css"
# app_include_js = "/assets/papers/js/papers.js"
app_include_js = [
    # "papers.bundle.js"
]

# include js, css files in header of web template
# web_include_css = "/assets/papers/css/papers.css"
# web_include_js = "/assets/papers/js/papers.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "papers/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

doctype_js={
	"Sales Invoice":"public/sales_invoice.js",
	 "Sales Order": "public/sales_order.js",
	 "Purchase Order": "public/purchase_order.js",
	 "Delivery Note": "public/Delivery_Note.js",
	 "Purchase Receipt": "public/Purchase_Receipt.js",
	 "Purchase Invoice": "public/purchase_invoice.js",
     "Material Request": "public/material_request.js",
     
	}
# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "papers.install.before_install"
# after_install = "papers.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "papers.uninstall.before_uninstall"
# after_uninstall = "papers.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "papers.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }
override_doctype_class = {
	"Material Request": "papers.doc_events.material_request.CustomMaterialRequest"
}
# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	# "*": {
# 	# 	"on_update": "method",
# 	# 	"on_cancel": "method",
# 	# 	"on_trash": "method"
# 	# }
#   "Sales Invoice":
#   {

# }
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"papers.tasks.all"
# 	],
# 	"daily": [
# 		"papers.tasks.daily"
# 	],
# 	"hourly": [
# 		"papers.tasks.hourly"
# 	],
# 	"weekly": [
# 		"papers.tasks.weekly"
# 	]
# 	"monthly": [
# 		"papers.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "papers.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "papers.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "papers.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]


# User Data Protection
# --------------------

user_data_fields = [
	{
		"doctype": "{doctype_1}",
		"filter_by": "{filter_by}",
		"redact_fields": ["{field_1}", "{field_2}"],
		"partial": 1,
	},
	{
		"doctype": "{doctype_2}",
		"filter_by": "{filter_by}",
		"partial": 1,
	},
	{
		"doctype": "{doctype_3}",
		"strict": False,
	},
	{
		"doctype": "{doctype_4}"
	}
]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"papers.auth.validate"
# ]

# Translation
# --------------------------------

# Make link fields search translated document names for these DocTypes
# Recommended only for DocTypes which have limited documents with untranslated names
# For example: Role, Gender, etc.
# translated_search_doctypes = []



# batch valuation override

# from papers.batch_valuation_overrides import get_supplied_items_cost,set_incoming_rate_buying,set_incoming_rate_selling,get_rate_for_return,get_incoming_rate,process_sle,get_args_for_incoming_rate

# # Buying controllers
# from erpnext.controllers.buying_controller import BuyingController
# BuyingController.get_supplied_items_cost = get_supplied_items_cost
# BuyingController.set_incoming_rate = set_incoming_rate_buying

# # Selling controllers
# from erpnext.controllers.selling_controller import SellingController
# SellingController.set_incoming_rate = set_incoming_rate_selling

# # sales and purchase return
# from erpnext.controllers import sales_and_purchase_return
# sales_and_purchase_return.get_rate_for_return =  get_rate_for_return

# # Document Events
# # ---------------
# # Hook on document methods and events
# import erpnext
# erpnext.stock.utils.get_incoming_rate = get_incoming_rate

# # stock_ledger
# from erpnext.stock.stock_ledger import update_entries_after
# update_entries_after.process_sle =  process_sle

# # stock entry
# from erpnext.stock.doctype.stock_entry.stock_entry import StockEntry
# StockEntry.get_args_for_incoming_rate = get_args_for_incoming_rate

doc_events = {
	# "Batch": {
	# 	'before_naming': "papers.batch_valuation.override_batch_autoname",
	# },
	# "Purchase Receipt": {
	# 	"validate": [
	# 		"papers.batch_valuation.pr_validate",
			

	# 	],
	# 	"on_cancel": "papers.batch_valuation.pr_on_cancel",
		
	# },
	# "Purchase Invoice": {
	# 	"validate": [
	# 		"papers.batch_valuation.pi_validate",
			

	# 		],
	# 	"on_cancel": "papers.batch_valuation.pi_on_cancel",
		
	# },
	# "Landed Cost Voucher": {
	# 	"validate": [
	# 		"papers.batch_valuation.lcv_validate",
	# 	],
	# 	"on_submit": "papers.batch_valuation.lcv_on_submit",
	# 	"on_cancel": [
	# 		"papers.batch_valuation.lcv_on_cancel",
	# 	],
	# },
# 	"Stock Entry": {
# 		"validate": [
# 			"papers.batch_valuation.stock_entry_validate",
# 		],
# # 		"before_save": "surgical.api.stock_entry_before_save",
# 		"on_submit": [
# 			"papers.batch_valuation.stock_entry_on_submit",
# 		],
# 		"on_cancel": [
# 			"papers.batch_valuation.stock_entry_on_cancel",
# 		],
# 	},
	"Item":{
		"validate":"papers.items.validation",
	},	
    "Batch":{
    		"before_naming":"papers.api.before_naming"
	},
    "Journal Entry": {
        "before_submit": "papers.doc_events.journal_entry.je_validate"
	}	
}

#e invoice override
import erpnext

# from papers.e_invoice_override import update_invoice_taxes,get_invoice_value_details
# erpnext.regional.india.e_invoice.utils.update_invoice_taxes = update_invoice_taxes
# erpnext.regional.india.e_invoice.utils.get_invoice_value_details = get_invoice_value_details

#Item variant
from papers.item_variant_overrides import make_variant_item_code_with_variant_name,copy_attributes_to_variant as copy_attributes,update_variants,update_variants_enqueue, validate_is_incremental as validate_is_incremental_papers
from erpnext.controllers import item_variant  
item_variant.make_variant_item_code = make_variant_item_code_with_variant_name
item_variant.copy_attributes_to_variant = copy_attributes
item_variant.validate_is_incremental = validate_is_incremental_papers

from erpnext.stock.doctype.item import item
item.update_variants = update_variants

from erpnext.stock.doctype.item.item import Item
Item.update_variants = update_variants_enqueue

