from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"label": _("Settings"),
			"icon": "octicon octicon-tools",
			"items": [
				{
					"type": "doctype",
					"name": "Stats Intranet",
					"description": _("Settings for the Stats Intranet"),
					"onboard": 1,
				},
				{
					"type": "doctype",
					"name": "File",
					"label": _("Files"),
				},
			]
		},
	]