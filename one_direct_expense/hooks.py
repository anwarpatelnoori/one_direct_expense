app_name = "one_direct_expense"
app_title = "One Direct Expense"
app_publisher = "anwarpatelrazvi@gmail.com"
app_description = "One Direct Expense"
app_email = "anwarpatelrazvi@gmail.com"
app_license = "mit"

# Apps
# ------------------

# required_apps = []

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "one_direct_expense",
# 		"logo": "/assets/one_direct_expense/logo.png",
# 		"title": "One Direct Expense",
# 		"route": "/one_direct_expense",
# 		"has_permission": "one_direct_expense.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/one_direct_expense/css/one_direct_expense.css"
# app_include_js = "/assets/one_direct_expense/js/one_direct_expense.js"

# include js, css files in header of web template
# web_include_css = "/assets/one_direct_expense/css/one_direct_expense.css"
# web_include_js = "/assets/one_direct_expense/js/one_direct_expense.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "one_direct_expense/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
doctype_js = {
    "Purchase Invoice": "one_direct_expense/overrides/purchase_invoice/custom_purchase_invoice.js"
}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "one_direct_expense/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "one_direct_expense.utils.jinja_methods",
# 	"filters": "one_direct_expense.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "one_direct_expense.install.before_install"
# after_install = "one_direct_expense.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "one_direct_expense.uninstall.before_uninstall"
# after_uninstall = "one_direct_expense.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "one_direct_expense.utils.before_app_install"
# after_app_install = "one_direct_expense.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "one_direct_expense.utils.before_app_uninstall"
# after_app_uninstall = "one_direct_expense.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "one_direct_expense.notifications.get_notification_config"

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
fixtures = [
    {
        "dt": "Item",
        "filters": [
            ["name", "=", "Direct Purchase"]
        ]
    },
    {
        "dt":"Item Group",
        "filters":[
            ["name", "=", "Direct Purchase"]
        ]
    }
]
# DocType Class
# ---------------
# Override standard doctype classes

override_doctype_class = {
    "Purchase Invoice": "one_direct_expense.one_direct_expense.overrides.purchase_invoice.custom_purchase_invoice.CustomPurchaseInvoice"
}

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"one_direct_expense.tasks.all"
# 	],
# 	"daily": [
# 		"one_direct_expense.tasks.daily"
# 	],
# 	"hourly": [
# 		"one_direct_expense.tasks.hourly"
# 	],
# 	"weekly": [
# 		"one_direct_expense.tasks.weekly"
# 	],
# 	"monthly": [
# 		"one_direct_expense.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "one_direct_expense.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "one_direct_expense.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "one_direct_expense.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["one_direct_expense.utils.before_request"]
# after_request = ["one_direct_expense.utils.after_request"]

# Job Events
# ----------
# before_job = ["one_direct_expense.utils.before_job"]
# after_job = ["one_direct_expense.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"one_direct_expense.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

# Translation
# ------------
# List of apps whose translatable strings should be excluded from this app's translations.
# ignore_translatable_strings_from = []

