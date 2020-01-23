import frappe
from frappe.utils import now
from frappe import _

no_cache = 1
no_sitemap = 1

def get_context(context):
    context.slide_show_images = frappe.db.sql("select file_url, file_name from `tabFile` where image_for='Slide Show' and is_private = 1", as_dict=True)
    context.icons = frappe.db.sql("select file_url, path_to_url from `tabFile` where image_for='Icon' and is_private = 1", as_dict=True)