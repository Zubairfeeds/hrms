# # Copyright (c) 2024, Frappe Technologies Pvt. Ltd. and contributors
# # For license information, please see license.txt

# # import frappe


# # def execute(filters=None):
# # 	columns, data = [], []
# # 	return columns, data
# # Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# # License: GNU General Public License v3. See license.txt


# import frappe
# from itertools import groupby
# from frappe import _
# from frappe.utils import flt
# from typing import Dict, List, Optional, Tuple


# import erpnext
# Filters = frappe._dict

# salary_slip = frappe.qb.DocType("Salary Slip")
# salary_detail = frappe.qb.DocType("Salary Detail")
# salary_component = frappe.qb.DocType("Salary Component")


# # def execute(filters=None):
# #     if filters is None:
# #         filters = {}

# #     currency = None
# #     if filters.get("currency"):
# #         currency = filters.get("currency")
# #     company_currency = erpnext.get_company_currency(filters.get("company"))

# #     salary_slips = get_salary_slips(filters, company_currency)
# #     if not salary_slips:
# #         return [], []

# #     earning_types, ded_types = get_earning_and_deduction_types(salary_slips)
# #     columns = get_columns(filters, earning_types, ded_types)

# #     ss_earning_map = get_salary_slip_details(salary_slips, currency, company_currency, "earnings")
# #     ss_ded_map = get_salary_slip_details(salary_slips, currency, company_currency, "deductions")

# #     doj_map = get_employee_doj_map()

# #     data = []
# #     current_group_value = None  # Track current group-by value
# #     for ss in salary_slips:
# #         row = {
# #             "salary_slip_id": ss.name,
# #             "employee": ss.employee,
# #             "employee_name": ss.employee_name,
# #             "data_of_joining": doj_map.get(ss.employee),
# #             "branch": ss.branch,
# #             "department": ss.department,
# #             "designation": ss.designation,
# #             "company": ss.company,
# #             "start_date": ss.start_date,
# #             "end_date": ss.end_date,
# #             "leave_without_pay": ss.leave_without_pay,
# #             "payment_days": ss.payment_days,
# #             "currency": currency or company_currency,
# #             "total_loan_repayment": ss.total_loan_repayment,
# #         }

# #         update_column_width(ss, columns)

# #         for e in earning_types:
# #             row.update({frappe.scrub(e): ss_earning_map.get(ss.name, {}).get(e)})

# #         for d in ded_types:
# #             row.update({frappe.scrub(d): ss_ded_map.get(ss.name, {}).get(d)})

# #         if currency == company_currency:
# #             row.update(
# #                 {
# #                     "gross_pay": flt(ss.gross_pay) * flt(ss.exchange_rate),
# #                     "total_deduction": flt(ss.total_deduction) * flt(ss.exchange_rate),
# #                     "net_pay": flt(ss.net_pay) * flt(ss.exchange_rate),
# #                 }
# #             )

# #         else:
# #             row.update(
# #                 {"gross_pay": ss.gross_pay, "total_deduction": ss.total_deduction, "net_pay": ss.net_pay}
# #             )

# #         if filters.get("group_by"):
# #             group_value = row.get(filters.get("group_by").lower())
# #             if group_value != current_group_value:
# #                 # Start a new row with group-by value
# #                 data.append({filters.get("group_by"): group_value})
# #                 current_group_value = group_value

# #         data.append(row)

# #     return columns, data


# def execute(filters=None):
#     if filters is None:
#         filters = {}

#     currency = None
#     if filters.get("currency"):
#         currency = filters.get("currency")
#     company_currency = erpnext.get_company_currency(filters.get("company"))

#     salary_slips = get_salary_slips(filters, company_currency)
#     if not salary_slips:
#         return [], []

#     earning_types, ded_types = get_earning_and_deduction_types(salary_slips)
#     columns = get_columns(filters, earning_types, ded_types)

#     ss_earning_map = get_salary_slip_details(salary_slips, currency, company_currency, "earnings")
#     ss_ded_map = get_salary_slip_details(salary_slips, currency, company_currency, "deductions")

#     doj_map = get_employee_doj_map()

#     data = []
#     current_group_value = None  # Track current group-by value
#     group_total_earnings = {}
#     group_total_deductions = {}
    
#     for ss in salary_slips:
#         row = {
#             "salary_slip_id": ss.name,
#             "employee": ss.employee,
#             "employee_name": ss.employee_name,
#             "data_of_joining": doj_map.get(ss.employee),
#             "branch": ss.branch,
#             "department": ss.department,
#             "designation": ss.designation,
#             "company": ss.company,
#             "start_date": ss.start_date,
#             "end_date": ss.end_date,
#             "leave_without_pay": ss.leave_without_pay,
#             "payment_days": ss.payment_days,
#             "currency": currency or company_currency,
#             "total_loan_repayment": ss.total_loan_repayment,
#         }

#         update_column_width(ss, columns)

#         for e in earning_types:
#             amount = ss_earning_map.get(ss.name, {}).get(e, 0)
#             row.update({frappe.scrub(e): amount})
#             group_total_earnings[e] = group_total_earnings.get(e, 0) + amount

#         for d in ded_types:
#             amount = ss_ded_map.get(ss.name, {}).get(d, 0)
#             row.update({frappe.scrub(d): amount})
#             group_total_deductions[d] = group_total_deductions.get(d, 0) + amount

#         if filters.get("group_by"):
#             group_value = row.get(filters.get("group_by").lower())
#             if group_value != current_group_value:
#                 # Start a new row with group-by value
#                 if current_group_value is not None:
#                     # Append group-wise total row for the previous group
#                     data.append(get_group_total_row(earning_types, ded_types, group_total_earnings, group_total_deductions))
#                     group_total_earnings = {}
#                     group_total_deductions = {}
                
#                 data.append({filters.get("group_by"): group_value})
#                 current_group_value = group_value

#         data.append(row)
    
#     # Append the last group-wise total row
#     if current_group_value is not None:
#         data.append(get_group_total_row(earning_types, ded_types, group_total_earnings, group_total_deductions))

#     return columns, data

# def get_group_total_row(earning_types, ded_types, group_total_earnings, group_total_deductions):
#     row = {"salary_slip_id": _("Group Total")}
#     for e in earning_types:
#         row.update({frappe.scrub(e): group_total_earnings.get(e, 0)})
#     row.update({"gross_pay": sum(group_total_earnings.values())})
#     for d in ded_types:
#         row.update({frappe.scrub(d): group_total_deductions.get(d, 0)})
#     row.update({"total_deduction": sum(group_total_deductions.values())})
#     row.update({"net_pay": row["gross_pay"] - row["total_deduction"]})
#     return row




# def get_earning_and_deduction_types(salary_slips):
# 	salary_component_and_type = {_("Earning"): [], _("Deduction"): []}

# 	for salary_compoent in get_salary_components(salary_slips):
# 		component_type = get_salary_component_type(salary_compoent)
# 		salary_component_and_type[_(component_type)].append(salary_compoent)

# 	return sorted(salary_component_and_type[_("Earning")]), sorted(
# 		salary_component_and_type[_("Deduction")]
# 	)


# def update_column_width(ss, columns):
# 	if ss.branch is not None:
# 		columns[3].update({"width": 120})
# 	if ss.department is not None:
# 		columns[4].update({"width": 120})
# 	if ss.designation is not None:
# 		columns[5].update({"width": 120})
# 	if ss.leave_without_pay is not None:
# 		columns[9].update({"width": 120})

# def get_columns(filters: Filters, earning_types, ded_types) -> List[Dict]:

#     columns = [
#         {
#             "label": _("Salary Slip ID"),
#             "fieldname": "salary_slip_id",
#             "fieldtype": "Link",
#             "options": "Salary Slip",
#             "width": 150,
#         },
#         {
#             "label": _("Employee"),
#             "fieldname": "employee",
#             "fieldtype": "Link",
#             "options": "Employee",
#             "width": 200,
#         },
#         {
#             "label": _("Employee Name"),
#             "fieldname": "employee_name",
#             "fieldtype": "Data",
#             "width": 140,
#         },
#         {
#             "label": _("Date of Joining"),
#             "fieldname": "data_of_joining",
#             "fieldtype": "Date",
#             "width": 80,
#         },
#         {
#             "label": _("Company"),
#             "fieldname": "company",
#             "fieldtype": "Link",
#             "options": "Company",
#             "width": 120,
#         },
#         {
#             "label": _("Start Date"),
#             "fieldname": "start_date",
#             "fieldtype": "Data",
#             "width": 80,
#         },
#         {
#             "label": _("End Date"),
#             "fieldname": "end_date",
#             "fieldtype": "Data",
#             "width": 80,
#         },
#         {
#             "label": _("Leave Without Pay"),
#             "fieldname": "leave_without_pay",
#             "fieldtype": "Float",
#             "width": 50,
#         },
#         {
#             "label": _("Worked Days"),
#             "fieldname": "payment_days",
#             "fieldtype": "Float",
#             "width": 120,
#         },
#     ]
#         # Inserting new column based on group_by filter
#     if filters.group_by:
#         group_by_lower = filters.group_by.lower()
#         if group_by_lower == "branch":
#             columns.insert(0, {"label": "Branch", "fieldname": "branch", "fieldtype": "Data", "width": 150, "align": "left"})
#         elif group_by_lower == "department":
#             columns.insert(0, {"label": "Department", "fieldname": "department", "fieldtype": "Data", "width": 150, "align": "left"})
#         # elif group_by_lower == "section":
#         #     columns.insert(0, {"label": "Section", "fieldname": "section", "fieldtype": "Data", "width": 150, "align": "left"})
            
#     for earning in earning_types:
#         columns.append(
#             {
#                 "label": earning,
#                 "fieldname": frappe.scrub(earning),
#                 "fieldtype": "Currency",
#                 "options": "currency",
#                 "width": 120,
#             }
#         )

#     columns.append(
#         {
#             "label": _("Gross Payable"),
#             "fieldname": "gross_pay",
#             "fieldtype": "Currency",
#             "options": "currency",
#             "width": 120,
#         }
#     )

#     for deduction in ded_types:
#         columns.append(
#             {
#                 "label": deduction,
#                 "fieldname": frappe.scrub(deduction),
#                 "fieldtype": "Currency",
#                 "options": "currency",
#                 "width": 120,
#             }
#         )

#     columns.extend(
#         [
#             {
#                 "label": _("Loan Repayment"),
#                 "fieldname": "total_loan_repayment",
#                 "fieldtype": "Currency",
#                 "options": "currency",
#                 "width": 120,
#             },
#             {
#                 "label": _("Total Deduction"),
#                 "fieldname": "total_deduction",
#                 "fieldtype": "Currency",
#                 "options": "currency",
#                 "width": 120,
#             },
#             {
#                 "label": _("Net Payable"),
#                 "fieldname": "net_pay",
#                 "fieldtype": "Currency",
#                 "options": "currency",
#                 "width": 120,
#             },
#             {
#                 "label": _("Currency"),
#                 "fieldtype": "Data",
#                 "fieldname": "currency",
#                 "options": "Currency",
#                 "hidden": 1,
#             },
#         ]
#     )

#     return columns


# def get_salary_components(salary_slips):
# 	return (
# 		frappe.qb.from_(salary_detail)
# 		.where((salary_detail.amount != 0) & (salary_detail.parent.isin([d.name for d in salary_slips])))
# 		.select(salary_detail.salary_component)
# 		.distinct()
# 	).run(pluck=True)


# def get_salary_component_type(salary_component):
# 	return frappe.db.get_value("Salary Component", salary_component, "type", cache=True)


# def get_salary_slips(filters, company_currency):
# 	doc_status = {"Draft": 0, "Submitted": 1, "Cancelled": 2}

# 	query = frappe.qb.from_(salary_slip).select(salary_slip.star)

# 	if filters.get("docstatus"):
# 		query = query.where(salary_slip.docstatus == doc_status[filters.get("docstatus")])

# 	if filters.get("from_date"):
# 		query = query.where(salary_slip.start_date >= filters.get("from_date"))

# 	if filters.get("to_date"):
# 		query = query.where(salary_slip.end_date <= filters.get("to_date"))

# 	if filters.get("company"):
# 		query = query.where(salary_slip.company == filters.get("company"))

# 	if filters.get("employee"):
# 		query = query.where(salary_slip.employee == filters.get("employee"))

# 	if filters.get("department"):
# 		query = query.where(salary_slip.department == filters.get("department"))	
	
# 	if filters.get("branch"):
# 		query = query.where(salary_slip.branch == filters.get("branch"))				

# 	if filters.get("section"):
# 		query = query.where(salary_slip.section == filters.get("section"))				


# 	if filters.get("currency") and filters.get("currency") != company_currency:
# 		query = query.where(salary_slip.currency == filters.get("currency"))

# 	salary_slips = query.run(as_dict=1)

# 	return salary_slips or []


# def get_employee_doj_map():
# 	employee = frappe.qb.DocType("Employee")

# 	result = (frappe.qb.from_(employee).select(employee.name, employee.date_of_joining)).run()

# 	return frappe._dict(result)


# def get_salary_slip_details(salary_slips, currency, company_currency, component_type):
# 	salary_slips = [ss.name for ss in salary_slips]

# 	result = (
# 		frappe.qb.from_(salary_slip)
# 		.join(salary_detail)
# 		.on(salary_slip.name == salary_detail.parent)
# 		.where((salary_detail.parent.isin(salary_slips)) & (salary_detail.parentfield == component_type))
# 		.select(
# 			salary_detail.parent,
# 			salary_detail.salary_component,
# 			salary_detail.amount,
# 			salary_slip.exchange_rate,
# 		)
# 	).run(as_dict=1)

# 	ss_map = {}

# 	for d in result:
# 		ss_map.setdefault(d.parent, frappe._dict()).setdefault(d.salary_component, 0.0)
# 		if currency == company_currency:
# 			ss_map[d.parent][d.salary_component] += flt(d.amount) * flt(
# 				d.exchange_rate if d.exchange_rate else 1
# 			)
# 		else:
# 			ss_map[d.parent][d.salary_component] += flt(d.amount)

# 	return ss_map


# ############################################################


# def get_rows(employee_details, filters):
#     rows = []
#     # Check if employee_details is a dictionary
#     if isinstance(employee_details, dict):
#         # Iterate over the values of the dictionary
#         for emp in employee_details.values():
#             row = {
                
#             }
#             rows.append(row)
#     return rows



# def get_data(filters: Filters) -> List[Dict]:
#     employee_details, group_by_param_values = get_employee_related_details(filters.group_by, filters.company)
#     data = []

#     if filters.group_by:
#         group_by_column = frappe.scrub(filters.group_by)
#         for value in group_by_param_values:
#             if not value:
#                 continue
#             records = get_rows(employee_details[value], filters)
#             if records:
#                 data.append({group_by_column: frappe.bold(value), "branch_total": sum(record.get("branch_total", 0) for record in records)})
#                 data.extend(records)
#     else:
#         data = get_rows(employee_details, filters)

#     return data


# def get_employee_related_details(group_by: str, company: str) -> Tuple[Dict, List]:
#     """Returns
#     1. nested dict for employee details
#     2. list of values for the group by filter
#     """
#     Employee = frappe.qb.DocType("Employee")
#     query = (
#         frappe.qb.from_(Employee)
#         .select(
#             Employee.name,
#             Employee.employee_name,
#             Employee.designation,
#             Employee.department,
#             Employee.branch,
#             Employee.company,
#         )
#         .where(Employee.company == company)
#     )

#     if group_by:
#         group_by = group_by.lower()
#         query = query.orderby(group_by)

#     employee_details = query.run(as_dict=True)

#     group_by_param_values = []
#     emp_map = {}

#     if group_by:
#         for parameter, employees in groupby(employee_details, key=lambda d: d[group_by]):
#             group_by_param_values.append(parameter)
#             emp_map.setdefault(parameter, frappe._dict())

#             for emp in employees:
#                 emp_map[parameter][emp.name] = emp
#     else:
#         for emp in employee_details:
#             emp_map[emp.name] = emp

#     return emp_map, group_by_param_values
# def get_filters():
#     return [
#         {"fieldname": "group_by", "label": "Group By", "fieldtype": "Select", "options": ["", "Branch", "Department", "Section"]}
#     ]

# # Call the function with the desired group by parameter ('Department', 'Branch', or 'Section')
# # emp_details, group_by_values = get_employee_related_details('Department', 'YourCompany')








# Copyright (c) 2024, Frappe Technologies Pvt. Ltd. and contributors
# For license information, please see license.txt


import frappe
import erpnext
from itertools import groupby
from frappe import _
from frappe.utils import flt
from typing import Dict, List, Optional, Tuple





Filters = frappe._dict

salary_slip = frappe.qb.DocType("Salary Slip")
salary_detail = frappe.qb.DocType("Salary Detail")
salary_component = frappe.qb.DocType("Salary Component")


def execute(filters=None):
    if filters is None:
        filters = {}

    currency = filters.get("currency")
    company_currency = erpnext.get_company_currency(filters.get("company"))

    salary_slips = get_salary_slips(filters, company_currency)
    if not salary_slips:
        return [], []

    earning_types, ded_types = get_earning_and_deduction_types(salary_slips)
    columns = get_columns(filters, earning_types, ded_types)

    ss_earning_map = get_salary_slip_details(salary_slips, currency, company_currency, "earnings")
    ss_ded_map = get_salary_slip_details(salary_slips, currency, company_currency, "deductions")
    doj_map = get_employee_doj_map()

    data = []
    current_group_value = None

    # Initialize totals
    grand_total_earnings = {e: 0 for e in earning_types}
    grand_total_deductions = {d: 0 for d in ded_types}
    grand_total_leave_without_pay = 0
    grand_total_payment_days = 0
    grand_total_loan_repayment = 0

    group_total_earnings = {e: 0 for e in earning_types}
    group_total_deductions = {d: 0 for d in ded_types}
    group_total_leave_without_pay = 0
    group_total_payment_days = 0
    group_total_loan_repayment = 0

    # Sort salary slips based on the selected filter (branch or department)
    if filters.get("group_by"):
        if filters["group_by"].lower() == "branch":
            salary_slips.sort(key=lambda x: x.branch)
        elif filters["group_by"].lower() == "department":
            salary_slips.sort(key=lambda x: x.department)

    for ss in salary_slips:
        group_value = None
        if filters.get("group_by"):
            group_value = ss.branch if filters["group_by"].lower() == "branch" else ss.department

        if group_value != current_group_value:
            if current_group_value is not None:
                # Append the group total row if needed
                data.append(get_group_total_row(earning_types, ded_types, group_total_earnings, group_total_deductions, group_total_leave_without_pay, group_total_payment_days, group_total_loan_repayment))
                group_total_earnings = {e: 0 for e in earning_types}
                group_total_deductions = {d: 0 for d in ded_types}
                group_total_leave_without_pay = 0
                group_total_payment_days = 0
                group_total_loan_repayment = 0
            
            # Add the group label row
            if group_value:
                data.append({filters.get("group_by").lower(): frappe.bold(group_value)})
                current_group_value = group_value
            else:
                data.append({})

        row = {
            "salary_slip_id": ss.name,
            "employee": ss.employee,
            "employee_name": ss.employee_name,
            "data_of_joining": doj_map.get(ss.employee),
            "branch": ss.branch,
            "department": ss.department,
            "designation": ss.designation,
            "company": ss.company,
            "start_date": ss.start_date,
            "end_date": ss.end_date,
            "leave_without_pay": ss.leave_without_pay if ss.leave_without_pay is not None else 0,
            "payment_days": ss.payment_days if ss.payment_days is not None else 0,
            "currency": currency or company_currency,
            "total_loan_repayment": ss.total_loan_repayment if ss.total_loan_repayment is not None else 0,
            "gross_pay": ss.gross_pay,
            "total_deduction": ss.total_deduction,
            "net_pay": ss.net_pay,
        }

        # Add to grand totals
        grand_total_leave_without_pay += row["leave_without_pay"]
        grand_total_payment_days += row["payment_days"]
        grand_total_loan_repayment += row["total_loan_repayment"]

        # Add to group totals
        group_total_leave_without_pay += row["leave_without_pay"]
        group_total_payment_days += row["payment_days"]
        group_total_loan_repayment += row["total_loan_repayment"]

        for e in earning_types:
            amount = ss_earning_map.get(ss.name, {}).get(e, 0)
            row.update({frappe.scrub(e): amount})
            group_total_earnings[e] = group_total_earnings.get(e, 0) + amount
            grand_total_earnings[e] = grand_total_earnings.get(e, 0) + amount

        for d in ded_types:
            amount = ss_ded_map.get(ss.name, {}).get(d, 0)
            row.update({frappe.scrub(d): amount})
            group_total_deductions[d] = group_total_deductions.get(d, 0) + amount
            grand_total_deductions[d] = grand_total_deductions.get(d, 0) + amount

        data.append(row)

    # Append the last group-wise total row
    if current_group_value is not None:
        data.append(get_group_total_row(earning_types, ded_types, group_total_earnings, group_total_deductions, group_total_leave_without_pay, group_total_payment_days, group_total_loan_repayment))

    # Append the grand total row
    data.append(get_grand_total_row(earning_types, ded_types, grand_total_earnings, grand_total_deductions, grand_total_leave_without_pay, grand_total_payment_days, grand_total_loan_repayment))

    return columns, data



def get_group_total_row(earning_types, ded_types, group_total_earnings, group_total_deductions, group_total_leave_without_pay, group_total_payment_days, group_total_loan_repayment):
    row = {"salary_slip_id": _("Group Total")}
    for e in earning_types:
        row.update({frappe.scrub(e): group_total_earnings.get(e, 0)})
    row.update({"gross_pay": sum(group_total_earnings.values())})
    for d in ded_types:
        row.update({frappe.scrub(d): group_total_deductions.get(d, 0)})
    row.update({"total_deduction": sum(group_total_deductions.values())})
    row.update({"net_pay": row["gross_pay"] - row["total_deduction"]})
    row.update({"leave_without_pay": group_total_leave_without_pay})
    row.update({"payment_days": group_total_payment_days})
    row.update({"total_loan_repayment": group_total_loan_repayment})
    return row

def get_grand_total_row(earning_types, ded_types, grand_total_earnings, grand_total_deductions, grand_total_leave_without_pay, grand_total_payment_days, grand_total_loan_repayment):
    row = {"salary_slip_id": _("Grand Total")}
    for e in earning_types:
        row.update({frappe.scrub(e): grand_total_earnings.get(e, 0)})
    row.update({"gross_pay": sum(grand_total_earnings.values())})
    for d in ded_types:
        row.update({frappe.scrub(d): grand_total_deductions.get(d, 0)})
    row.update({"total_deduction": sum(grand_total_deductions.values())})
    row.update({"net_pay": row["gross_pay"] - row["total_deduction"]})
    row.update({"leave_without_pay": grand_total_leave_without_pay})
    row.update({"payment_days": grand_total_payment_days})
    row.update({"total_loan_repayment": grand_total_loan_repayment})
    return row

def get_earning_and_deduction_types(salary_slips):
	salary_component_and_type = {_("Earning"): [], _("Deduction"): []}

	for salary_compoent in get_salary_components(salary_slips):
		component_type = get_salary_component_type(salary_compoent)
		salary_component_and_type[_(component_type)].append(salary_compoent)

	return sorted(salary_component_and_type[_("Earning")]), sorted(
		salary_component_and_type[_("Deduction")]
	)


# def update_column_width(ss, columns):
# 	if ss.branch is not None:
# 		columns[3].update({"width": 120})
# 	if ss.department is not None:
# 		columns[4].update({"width": 120})
# 	if ss.designation is not None:
# 		columns[5].update({"width": 120})
# 	if ss.leave_without_pay is not None:
# 		columns[9].update({"width": 120})
def get_columns(filters: Filters, earning_types, ded_types) -> List[Dict]:
    # Initialize columns list
    columns = [
        {
            "label": _("Salary Slip ID"),
            "fieldname": "salary_slip_id",
            "fieldtype": "Link",
            "options": "Salary Slip",
            "width": 150,
        },
        {
            "label": _("Employee"),
            "fieldname": "employee",
            "fieldtype": "Link",
            "options": "Employee",
            "width": 200,
        },
        {
            "label": _("Employee Name"),
            "fieldname": "employee_name",
            "fieldtype": "Data",
            "width": 140,
        },
        # {
        #     "label": _("Branch"),
        #     "fieldname": "branch",
        #     "fieldtype": "Link",
        #     "options": "Branch",
        #     "width": 120,
        # },
        # {
        #     "label": _("Department"),
        #     "fieldname": "department",
        #     "fieldtype": "Link",
        #     "options": "Department",
        #     "width": 120,
        # },
        {
            "label": _("Designation"),
            "fieldname": "designation",
            "fieldtype": "Link",
            "options": "Designation",
            "width": 120,
        },
        {
            "label": _("Date of Joining"),
            "fieldname": "data_of_joining",
            "fieldtype": "Date",
            "width": 80,
        },
        {
            "label": _("Company"),
            "fieldname": "company",
            "fieldtype": "Link",
            "options": "Company",
            "width": 120,
        },
        {
            "label": _("Leave Without Pay"),
            "fieldname": "leave_without_pay",
            "fieldtype": "Float",
            "width": 100,
        },
        {
            "label": _("Worked Days"),
            "fieldname": "payment_days",
            "fieldtype": "Float",
            "width": 120,
        },
    ]

    # Determine the group_by filter
    # if filters.get("group_by"):
    #     group_by_lower = filters["group_by"].lower()
    #     if group_by_lower == "branch":
    #         columns.insert(0, {
    #             "label": _("Branch"),
    #             "fieldname": "branch",
    #             "fieldtype": "Link",
    #             "options": "Branch",
    #             "width": 120,
    #         })
    #     elif group_by_lower == "department":
    #         columns.insert(0, {
    #             "label": _("Department"),
    #             "fieldname": "department",
    #             "fieldtype": "Link",
    #             "options": "Department",
    #             "width": 120,
    #         })

    group_by = filters.get("group_by", "").lower()

    # Add group-by column based on filter
    if group_by == "branch":
        columns.insert(0, 
        {  # Insert after Employee Name
            "label": _("Branch"),
            "fieldname": "branch",
            "fieldtype": "Link",
            "options": "Branch",
            "width": 120,
        })
        columns.insert(4,
        {  # Insert after Employee Name
            "label": _("Department"),
            "fieldname": "department",
            "fieldtype": "Link",
            "options": "Department",
            "width": 120,
        })
    elif group_by == "department":
        columns.insert(0, 
        {  # Insert after Employee Name
            "label": _("Department"),
            "fieldname": "department",
            "fieldtype": "Link",
            "options": "Department",
            "width": 120,
        })
        columns.insert(4, {  # Insert after Employee Name
            "label": _("Branch"),
            "fieldname": "branch",
            "fieldtype": "Link",
            "options": "Branch",
            "width": 120,
        })
    else:
        # Show both columns if no filter is selected
        columns.insert(3, {  # Insert after Employee Name
            "label": _("Branch"),
            "fieldname": "branch",
            "fieldtype": "Link",
            "options": "Branch",
            "width": 120,
        })
        columns.insert(4, {  # Insert after Branch
            "label": _("Department"),
            "fieldname": "department",
            "fieldtype": "Link",
            "options": "Department",
            "width": 120,
        })

    # Add earning columns
    for earning in earning_types:
        column = {
            "label": earning,
            "fieldname": frappe.scrub(earning),
            "fieldtype": "Currency",
            "width": 120,
        }
        if filters.get("currency") or erpnext.get_company_currency(filters.get("company")):
            column["options"] = "currency"
        columns.append(column)

    columns.append(
        {
            "label": _("Gross Payable"),
            "fieldname": "gross_pay",
            "fieldtype": "Currency",
            "width": 120,
        }
    )

    # Add deduction columns
    for deduction in ded_types:
        column = {
            "label": deduction,
            "fieldname": frappe.scrub(deduction),
            "fieldtype": "Currency",
            "width": 120,
        }
        if filters.get("currency") or erpnext.get_company_currency(filters.get("company")):
            column["options"] = "currency"
        columns.append(column)

    columns += [
        {
            "label": _("Loan Repayment"),
            "fieldname": "total_loan_repayment",
            "fieldtype": "Currency",
            "width": 120,
        },
        {
            "label": _("Total Deductions"),
            "fieldname": "total_deduction",
            "fieldtype": "Currency",
            "width": 120,
        },
        {
            "label": _("Net Pay"),
            "fieldname": "net_pay",
            "fieldtype": "Currency",
            "width": 120,
        },
    ]

    return columns




def get_salary_components(salary_slips):
	return (
		frappe.qb.from_(salary_detail)
		.where((salary_detail.amount != 0) & (salary_detail.parent.isin([d.name for d in salary_slips])))
		.select(salary_detail.salary_component)
		.distinct()
	).run(pluck=True)


def get_salary_component_type(salary_component):
	return frappe.db.get_value("Salary Component", salary_component, "type", cache=True)


def get_salary_slips(filters, company_currency):
	doc_status = {"Draft": 0, "Submitted": 1, "Cancelled": 2}

	query = frappe.qb.from_(salary_slip).select(salary_slip.star)

	if filters.get("docstatus"):
		query = query.where(salary_slip.docstatus == doc_status[filters.get("docstatus")])

	if filters.get("from_date"):
		query = query.where(salary_slip.start_date >= filters.get("from_date"))

	if filters.get("to_date"):
		query = query.where(salary_slip.end_date <= filters.get("to_date"))

	if filters.get("company"):
		query = query.where(salary_slip.company == filters.get("company"))

	if filters.get("employee"):
		query = query.where(salary_slip.employee == filters.get("employee"))

	if filters.get("department"):
		query = query.where(salary_slip.department == filters.get("department"))	
	
	if filters.get("branch"):
		query = query.where(salary_slip.branch == filters.get("branch"))				

	if filters.get("section"):
		query = query.where(salary_slip.section == filters.get("section"))				


	if filters.get("currency") and filters.get("currency") != company_currency:
		query = query.where(salary_slip.currency == filters.get("currency"))

	salary_slips = query.run(as_dict=1)

	return salary_slips or []


def get_employee_doj_map():
	employee = frappe.qb.DocType("Employee")

	result = (frappe.qb.from_(employee).select(employee.name, employee.date_of_joining)).run()

	return frappe._dict(result)


def get_salary_slip_details(salary_slips, currency, company_currency, component_type):
	salary_slips = [ss.name for ss in salary_slips]

	result = (
		frappe.qb.from_(salary_slip)
		.join(salary_detail)
		.on(salary_slip.name == salary_detail.parent)
		.where((salary_detail.parent.isin(salary_slips)) & (salary_detail.parentfield == component_type))
		.select(
			salary_detail.parent,
			salary_detail.salary_component,
			salary_detail.amount,
			salary_slip.exchange_rate,
		)
	).run(as_dict=1)

	ss_map = {}

	for d in result:
		ss_map.setdefault(d.parent, frappe._dict()).setdefault(d.salary_component, 0.0)
		if currency == company_currency:
			ss_map[d.parent][d.salary_component] += flt(d.amount) * flt(
				d.exchange_rate if d.exchange_rate else 1
			)
		else:
			ss_map[d.parent][d.salary_component] += flt(d.amount)

	return ss_map


############################################################


def get_rows(employee_details, filters):
    rows = []
    # Check if employee_details is a dictionary
    if isinstance(employee_details, dict):
        # Iterate over the values of the dictionary
        for emp in employee_details.values():
            row = {
                
            }
            rows.append(row)
    return rows



def get_data(filters: Filters) -> List[Dict]:
    employee_details, group_by_param_values = get_employee_related_details(filters.group_by, filters.company)
    data = []

    if filters.group_by:
        group_by_column = frappe.scrub(filters.group_by)
        for value in group_by_param_values:
            if not value:
                continue
            records = get_rows(employee_details[value], filters)
            if records:
                data.append({group_by_column: frappe.bold(value), "branch_total": sum(record.get("branch_total", 0) for record in records)})
                data.extend(records)
    else:
        data = get_rows(employee_details, filters)

    return data


def get_employee_related_details(group_by: str, company: str) -> Tuple[Dict, List]:
    """Returns
    1. nested dict for employee details
    2. list of values for the group by filter
    """
    Employee = frappe.qb.DocType("Employee")
    query = (
        frappe.qb.from_(Employee)
        .select(
            Employee.name,
            Employee.employee_name,
            Employee.designation,
            Employee.department,
            Employee.branch,
            Employee.company,
        )
        .where(Employee.company == company)
    )

    if group_by:
        group_by = group_by.lower()
        query = query.orderby(group_by)

    employee_details = query.run(as_dict=True)

    group_by_param_values = []
    emp_map = {}

    if group_by:
        for parameter, employees in groupby(employee_details, key=lambda d: d[group_by]):
            group_by_param_values.append(parameter)
            emp_map.setdefault(parameter, frappe._dict())

            for emp in employees:
                emp_map[parameter][emp.name] = emp
    else:
        for emp in employee_details:
            emp_map[emp.name] = emp

    return emp_map, group_by_param_values
def get_filters():
    return [
        {"fieldname": "group_by", "label": "Group By", "fieldtype": "Select", "options": ["", "Branch", "Department", "Section"]}
    ]

# Call the function with the desired group by parameter ('Department', 'Branch', or 'Section')
# emp_details, group_by_values = get_employee_related_details('Department', 'YourCompany')



