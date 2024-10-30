// Copyright (c) 2024, Frappe Technologies Pvt. Ltd. and contributors
// For license information, please see license.txt
/* eslint-disable */

// frappe.query_reports["Daily Attendance Summary"] = {
// 	"filters": [

// 	]
// };
frappe.query_reports["Daily Attendance Summary"] = {
	"filters": [
		{
			"fieldname": "from_date",
			"label": __("From Date"),
			"fieldtype": "Date",
			"default": frappe.datetime.get_today(),
			"reqd": 1,
		},
		{
			"fieldname": "to_date",
			"label": __("To Date"),
			"fieldtype": "Date",
			"default": frappe.datetime.get_today(),
			"reqd": 1,
		},
		{
			"fieldname": "branch",
			"label": __("Branch"),
			"fieldtype": "Link",
			"options": "Branch"
		},
		// {
		// 	"fieldname": "department_wise",
		// 	"label": __("Department Wise"),
		// 	"fieldtype": "Check"
		// },
		// {
		// 	"fieldname": "department",
		// 	"label": __("Department"),
		// 	"fieldtype": "Link",
		// 	"options": "Department",
		// 	"hidden": true
		// }
	],
	"onload": (report) => {
		report.page.add_inner_button(__('Refresh'), function () {
			report.refresh();
		});
	}
};
