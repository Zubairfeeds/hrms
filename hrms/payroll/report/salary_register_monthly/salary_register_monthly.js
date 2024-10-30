// // Copyright (c) 2024, Frappe Technologies Pvt. Ltd. and contributors
// // For license information, please see license.txt
// /* eslint-disable */

// // frappe.query_reports["Salary Register Monthly"] = {
// // 	"filters": [

// // 	]
// // };



// frappe.query_reports["Salary Register Monthly"] = {
// 	"filters": [
// 		{
// 			"fieldname": "from_date",
// 			"label": __("From"),
// 			"fieldtype": "Date",
// 			"default": frappe.datetime.add_months(frappe.datetime.get_today(), -1),
// 			"reqd": 1,
// 			"width": "100px"
// 		},
// 		{
// 			"fieldname": "to_date",
// 			"label": __("To"),
// 			"fieldtype": "Date",
// 			"default": frappe.datetime.get_today(),
// 			"reqd": 1,
// 			"width": "100px"
// 		},
// 		{
// 			"fieldname": "currency",
// 			"fieldtype": "Link",
// 			"options": "Currency",
// 			"label": __("Currency"),
// 			"default": erpnext.get_currency(frappe.defaults.get_default("Company")),
// 			"width": "50px"
// 		},
// 		{
// 			"fieldname": "employee",
// 			"label": __("Employee"),
// 			"fieldtype": "Link",
// 			"options": "Employee",
// 			"width": "200px"
// 		},
// 		{
//             "fieldname": "group_by",
//             "label": __("Group By"),
//             "fieldtype": "Select",
//             "options": ["", "Branch", "Department"],
//             "width": "100px"
//         },
// 		{
// 			"fieldname": "company",
// 			"label": __("Company"),
// 			"fieldtype": "Link",
// 			"options": "Company",
// 			"default": frappe.defaults.get_user_default("Company"),
// 			"width": "100px",
// 			"reqd": 1
// 		},
// 		{
// 			"fieldname": "docstatus",
// 			"label": __("Document Status"),
// 			"fieldtype": "Select",
// 			"options": ["Draft", "Submitted", "Cancelled"],
// 			"default": "Submitted",
// 			"width": "100px"
// 		}
// 	],
// 	// formatter: function(value, row, column, data, default_formatter) {
// 	// 	value = default_formatter(value, row, column, data);
// 	// 	const group_by = frappe.query_report.get_filter_value('group_by');

// 	// 	return value;
// 	// }
// }



// Copyright (c) 2024, Frappe Technologies Pvt. Ltd. and contributors
// For license information, please see license.txt
/* eslint-disable */

// frappe.query_reports["Salary Register Monthly"] = {
// 	"filters": [

// 	]
// };



frappe.query_reports["Salary Register Monthly"] = {
	"filters": [
		{
			"fieldname": "from_date",
			"label": __("From"),
			"fieldtype": "Date",
			"default": frappe.datetime.add_months(frappe.datetime.get_today(), -1),
			"reqd": 1,
			"width": "100px"
		},
		{
			"fieldname": "to_date",
			"label": __("To"),
			"fieldtype": "Date",
			"default": frappe.datetime.get_today(),
			"reqd": 1,
			"width": "100px"
		},
		{
			"fieldname": "currency",
			"fieldtype": "Link",
			"options": "Currency",
			"label": __("Currency"),
			"default": erpnext.get_currency(frappe.defaults.get_default("Company")),
			"width": "50px"
		},
		{
			"fieldname": "employee",
			"label": __("Employee"),
			"fieldtype": "Link",
			"options": "Employee",
			"width": "200px"
		},
		{
            "fieldname": "group_by",
            "label": __("Group By"),
            "fieldtype": "Select",
            "options": ["", "Branch", "Department"],
            "width": "100px"
        },
		{
			"fieldname": "company",
			"label": __("Company"),
			"fieldtype": "Link",
			"options": "Company",
			"default": frappe.defaults.get_user_default("Company"),
			"width": "100px",
			"reqd": 1
		},
		{
			"fieldname": "docstatus",
			"label": __("Document Status"),
			"fieldtype": "Select",
			"options": ["Draft", "Submitted", "Cancelled"],
			"default": "Submitted",
			"width": "100px"
		}
	],
	// formatter: function(value, row, column, data, default_formatter) {
	// 	value = default_formatter(value, row, column, data);
	// 	const group_by = frappe.query_report.get_filter_value('group_by');

	// 	return value;
	// }
}
