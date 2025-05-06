app_name = "nepali_date"
app_title = "Nepali Date"
app_publisher = "mukesh kr. chaudhary"
app_description = "Integrate Nepali date to ERPNext"
app_email = "mukesh@gmail.com"
app_license = "mit"

# Apps
# ------------------

# required_apps = []

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "nepali_date",
# 		"logo": "/assets/nepali_date/logo.png",
# 		"title": "Nepali Date",
# 		"route": "/nepali_date",
# 		"has_permission": "nepali_date.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/nepali_date/css/nepali_date.css"
app_include_css = ["/assets/nepali_date/css/calender.css",
                   "/assets/nepali_date/css/date.css"]
# app_include_js = "/assets/nepali_date/js/nepali_date.js"
app_include_js = [
    "/assets/nepali_date/js/bs_module.js",
    # "/assets/migration/js/report_filter.js",
    # "/assets/nepali_date/js/nepali_override.js",
    "/assets/nepali_date/js/nepali_override_with_sticktext.js",
    "/assets/nepali_date/js/nepali_formatter.js",
    # "/assets/nepali_date/js/print_override.js"
    "/assets/nepali_date/js/datetime_override.js", # Datetime override
    "/assets/nepali_date/js/datetime_formatter.js"
]
boot_session = ["nepali_date.boot.get_boot_info"]

# In hooks.py
override_whitelisted_methods = {
    "frappe.format_value": "nepali_date.date.format_value"
}
jinja = {
    "methods": ["nepali_date.date.format_value"]
}

# Override ERPNext reports (e.g., Monthly Purchase Register)
# override_whitelisted_methods = {
#     "frappe.desk.reportview.get": "nepali_date.report.monthly_purchase_register.get_report_data"
# }
# Register custom Jinja2 filters
# hooks.py

# jinja = {
#     "methods": [
#         "nepali_date.utils.convert_ad_to_bs"
#     ]
# }

# jinja = {
#     "methods": [
#         "nepali_date.overrides.jinja.inject_bs_formatter"
#     ]
# }
jenv = {
    "methods": ["nepali_date.utils.nepali_date.ad_to_bs_string"]
}


# include js, css files in header of web template
# web_include_css = "/assets/nepali_date/css/nepali_date.css"
# web_include_js = "/assets/nepali_date/js/nepali_date.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "nepali_date/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
doctype_js = {"User": "public/js/nepali_override.js",
              "Purchase Invoice": "public/js/utils.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "nepali_date/public/icons.svg"

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
# 	"methods": "nepali_date.utils.jinja_methods",
# 	"filters": "nepali_date.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "nepali_date.install.before_install"
after_install = "nepali_date.custom_field.create_custom_fields"
# after_install = "nepali_date.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "nepali_date.uninstall.before_uninstall"
# after_uninstall = "nepali_date.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "nepali_date.utils.before_app_install"
# after_app_install = "nepali_date.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "nepali_date.utils.before_app_uninstall"
# after_app_uninstall = "nepali_date.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "nepali_date.notifications.get_notification_config"

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
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"nepali_date.tasks.all"
# 	],
# 	"daily": [
# 		"nepali_date.tasks.daily"
# 	],
# 	"hourly": [
# 		"nepali_date.tasks.hourly"
# 	],
# 	"weekly": [
# 		"nepali_date.tasks.weekly"
# 	],
# 	"monthly": [
# 		"nepali_date.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "nepali_date.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "nepali_date.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "nepali_date.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["nepali_date.utils.before_request"]
# after_request = ["nepali_date.utils.after_request"]

# Job Events
# ----------
# before_job = ["nepali_date.utils.before_job"]
# after_job = ["nepali_date.utils.after_job"]

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
# 	"nepali_date.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

