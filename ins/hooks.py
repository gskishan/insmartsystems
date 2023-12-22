from . import __version__ as app_version

app_name = "ins"
app_title = "INS"
app_publisher = "Patel Asif Khan"
app_description = "insmartsystems"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "aasif.p@indictranstech.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/ins/css/ins.css"
# app_include_js = "/assets/ins/js/ins.js"

# include js, css files in header of web template
# web_include_css = "/assets/ins/css/ins.css"
# web_include_js = "/assets/ins/js/ins.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "ins/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views      

doctype_js = {"Enquiry":"public/js/enquiry.js"}


# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

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

# before_install = "ins.install.before_install"
# after_install = "ins.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "ins.uninstall.before_uninstall"
# after_uninstall = "ins.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "ins.notifications.get_notification_config"

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

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"ins.tasks.all"
# 	],
# 	"daily": [
# 		"ins.tasks.daily"
# 	],
# 	"hourly": [
# 		"ins.tasks.hourly"
# 	],
# 	"weekly": [
# 		"ins.tasks.weekly"
# 	]
# 	"monthly": [
# 		"ins.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "ins.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "ins.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "ins.task.get_dashboard_data"
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

doc_events = {
   "Sales Invoice" : {
		"before_save": "ins.custom_script.sales_invoice.before_save",
		
	},
}
# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"ins.auth.validate"
# ]

# Translation
# --------------------------------

# Make link fields search translated document names for these DocTypes
# Recommended only for DocTypes which have limited documents with untranslated names
# For example: Role, Gender, etc.
# translated_search_doctypes = []
