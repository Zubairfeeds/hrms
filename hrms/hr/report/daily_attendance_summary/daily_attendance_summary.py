# Copyright (c) 2024, Frappe Technologies Pvt. Ltd. and contributors
# For license information, please see license.txt

import frappe
from collections import defaultdict


def execute(filters=None):
    if filters.get("from_date") != filters.get("to_date"):
        frappe.throw("From Date and To Date should be the same")

    columns = [
        {"label": "Unit Name", "fieldname": "branch", "fieldtype": "Link", "options": "Branch", "width": 350},
        {"label": "Total Strength", "fieldname": "total_attendance_count", "fieldtype": "Int", "width": 150},
        {"label": "Present", "fieldname": "present_count", "fieldtype": "Int", "width": 100},
        {"label": "On Leave", "fieldname": "on_leave_count", "fieldtype": "Int", "width": 100},
        {"label": "Absent", "fieldname": "absent_count", "fieldtype": "Int", "width": 100}
    ]

    data = []

    if filters.get("from_date") and filters.get("to_date"):
        attendance_data = get_attendance_data(filters)
        data = list(attendance_data)

    return columns, data

def get_attendance_data(filters):
    attendance_counts = defaultdict(int)
    present_counts = defaultdict(int)
    on_leave_counts = defaultdict(int)
    absent_counts = defaultdict(int)

    total_employees = get_total_employees(filters.get("branch"))

    attendances = frappe.get_all("Attendance", filters=get_filters(filters), fields=["branch", "status", "employee"])
    for attendance in attendances:
        branch = attendance.get("branch")
        status = attendance.get("status")
        attendance_counts[branch] += 1
        if status == "Present":
            present_counts[branch] += 1
        elif status == "On Leave":
            on_leave_counts[branch] += 1
        elif status == "Absent":
            absent_counts[branch] += 1

    data = []
    for branch, employees_count in total_employees.items():
        data.append({
            "branch": branch,
            "total_attendance_count": employees_count,
            "present_count": present_counts.get(branch, 0),
            "on_leave_count": on_leave_counts.get(branch, 0),
            "absent_count": absent_counts.get(branch, 0)
        })

    return data

def get_filters(filters):
    attendance_filters = {"attendance_date": ["between", (filters.get("from_date"), filters.get("to_date"))]}
    if filters.get("branch"):
        attendance_filters["branch"] = filters.get("branch")
    return attendance_filters

def get_total_employees(selected_branch=None):
    total_employees = defaultdict(int)

    if selected_branch:
        employees = frappe.get_all("Employee", filters={"branch": selected_branch, "status": "Active"}, fields=["name"])
        total_employees[selected_branch] = len(employees)
    else:
        branches = frappe.get_all("Branch", fields=["name"])
        for branch in branches:
            employees = frappe.get_all("Employee", filters={"branch": branch.name, "status": "Active"}, fields=["name"])
            total_employees[branch.name] = len(employees)

    return total_employees




# def execute(filters=None):
#     if filters.get("from_date") != filters.get("to_date"):
#         frappe.throw("From Date and To Date should be the same")

#     columns = [
#         {"label": "Unit Name", "fieldname": "branch", "fieldtype": "Link", "options": "Branch", "width": 350},
#         {"label": "Total Strength", "fieldname": "total_attendance_count", "fieldtype": "Int", "width": 150},
#         {"label": "Present", "fieldname": "present_count", "fieldtype": "Int", "width": 100},
#         {"label": "On Leave", "fieldname": "on_leave_count", "fieldtype": "Int", "width": 100},
#         {"label": "Absent", "fieldname": "absent_count", "fieldtype": "Int", "width": 100}
#     ]

#     data = []

#     if filters.get("from_date") and filters.get("to_date"):
#         attendance_data = get_attendance_data(filters)
#         data = list(attendance_data)

#     return columns, data

# def get_attendance_data(filters):
#     attendance_counts = defaultdict(int)
#     present_counts = defaultdict(int)
#     on_leave_counts = defaultdict(int)
#     absent_counts = defaultdict(int)

#     total_employees = get_total_employees()

#     attendances = frappe.get_all("Attendance", filters=get_filters(filters), fields=["branch", "status", "employee"])
#     for attendance in attendances:
#         branch = attendance.get("branch")
#         status = attendance.get("status")
#         attendance_counts[branch] += 1
#         if status == "Present":
#             present_counts[branch] += 1
#         elif status == "On Leave":
#             on_leave_counts[branch] += 1
#         elif status == "Absent":
#             absent_counts[branch] += 1

#     data = []
#     for branch, employees_count in total_employees.items():
#         data.append({
#             "branch": branch,
#             "total_attendance_count": employees_count,
#             "present_count": present_counts.get(branch, 0),
#             "on_leave_count": on_leave_counts.get(branch, 0),
#             "absent_count": absent_counts.get(branch, 0)
#         })

#     return data

# def get_filters(filters):
#     attendance_filters = {"attendance_date": ["between", (filters.get("from_date"), filters.get("to_date"))]}
#     if filters.get("branch"):
#         attendance_filters["branch"] = filters.get("branch")
#     return attendance_filters

# def get_total_employees():
#     total_employees = defaultdict(int)

#     branches = frappe.get_all("Branch", fields=["name"])
#     for branch in branches:
#         employees = frappe.get_all("Employee", filters={"branch": branch.name}, fields=["name"])
#         total_employees[branch.name] = len(employees)

#     return total_employees




# def execute(filters=None):
#     if filters.get("from_date") != filters.get("to_date"):
#         frappe.throw("From Date and To Date should be the same")
#     columns = [
#         {"label": "Unit Name", "fieldname": "branch", "fieldtype": "Link", "options": "Branch", "width": 350},
#         {"label": "Total Strength", "fieldname": "total_attendance_count", "fieldtype": "Int", "width": 150},
#         {"label": "Present", "fieldname": "present_count", "fieldtype": "Int", "width": 100},
#         {"label": "On Leave", "fieldname": "on_leave_count", "fieldtype": "Int", "width": 100},
#         {"label": "Absent", "fieldname": "absent_count", "fieldtype": "Int", "width": 100}
#     ]

#     data = []

#     if filters.get("from_date") and filters.get("to_date"):
#         attendance_data = get_attendance_data(filters)
#         data = list(attendance_data)

#     return columns, data

# def get_attendance_data(filters):
#     attendance_counts = defaultdict(int)
#     present_counts = defaultdict(int)
#     on_leave_counts = defaultdict(int)
#     absent_counts = defaultdict(int)

#     total_employees = get_total_employees(filters.get("branch"))

#     attendances = frappe.get_all("Attendance", filters=get_filters(filters), fields=["branch", "status", "employee"])
#     for attendance in attendances:
#         branch = attendance.get("branch")
#         status = attendance.get("status")
#         attendance_counts[branch] += 1
#         if status == "Present":
#             present_counts[branch] += 1
#         elif status == "On Leave":
#             on_leave_counts[branch] += 1
#         elif status == "Absent":
#             absent_counts[branch] += 1

#     data = []
#     for branch in attendance_counts.keys():
#         data.append({
#             "branch": branch,
#             "total_attendance_count": total_employees[branch],
#             "present_count": present_counts[branch],
#             "on_leave_count": on_leave_counts[branch],
#             "absent_count": absent_counts[branch]
#         })

#     return data

# def get_filters(filters):
#     attendance_filters = {"attendance_date": ["between", (filters.get("from_date"), filters.get("to_date"))]}
#     if filters.get("branch"):
#         attendance_filters["branch"] = filters.get("branch")
#     return attendance_filters

# def get_total_employees(branch=None):
#     total_employees = defaultdict(int)

#     if branch:
#         employees = frappe.get_all("Employee", filters={"branch": branch}, fields=["name"])
#         total_employees[branch] = len(employees)
#     else:
#         branches = frappe.get_all("Branch", fields=["name"])
#         for branch in branches:
#             employees = frappe.get_all("Employee", filters={"branch": branch.name}, fields=["name"])
#             total_employees[branch.name] = len(employees)

#     return total_employees



# def execute(filters=None):
#     columns = [
#         {"label": "Unit Name", "fieldname": "branch", "fieldtype": "Link", "options": "Branch", "width": 350},
#         {"label": "Total Strength", "fieldname": "total_attendance_count", "fieldtype": "Int", "width": 150},
#         {"label": "Present", "fieldname": "present_count", "fieldtype": "Int", "width": 100},
#         {"label": "On Leave", "fieldname": "on_leave_count", "fieldtype": "Int", "width": 100},
#         {"label": "Absent", "fieldname": "absent_count", "fieldtype": "Int", "width": 100}
#     ]

#     data = []

#     if filters.get("from_date") and filters.get("to_date"):
#         branch = filters.get("branch")
#         attendance_data = get_attendance_data(filters.get("from_date"), filters.get("to_date"), branch)
#         data = list(attendance_data)

#     return columns, data

# def get_attendance_data(from_date, to_date, branch=None):
#     attendance_counts = defaultdict(int)
#     present_counts = defaultdict(int)
#     on_leave_counts = defaultdict(int)
#     absent_counts = defaultdict(int)

#     filters = {"attendance_date": ["between", (from_date, to_date)]}
#     if branch:
#         filters["branch"] = branch

#     attendances = frappe.get_all("Attendance", filters=filters, fields=["branch", "status", "employee"])
#     for attendance in attendances:
#         branch = attendance.get("branch")
#         status = attendance.get("status")
#         attendance_counts[branch] += 1
#         if status == "Present":
#             present_counts[branch] += 1
#         elif status == "On Leave":
#             on_leave_counts[branch] += 1
#         elif status == "Absent":
#             absent_counts[branch] += 1

#     data = []
#     for branch in attendance_counts.keys():
#         data.append({
#             "branch": branch,
#             "total_attendance_count": attendance_counts[branch],
#             "present_count": present_counts[branch],
#             "on_leave_count": on_leave_counts[branch],
#             "absent_count": absent_counts[branch]
#         })

#     return data


# def execute(filters=None):
#     columns = [
#         {"label": "Unit Name", "fieldname": "branch", "fieldtype": "Link", "options": "Branch", "width": 350},
#         {"label": "Total Strength", "fieldname": "total_attendance_count", "fieldtype": "Int", "width": 150},
#         {"label": "Present", "fieldname": "present_count", "fieldtype": "Int", "width": 100},
#         {"label": "On Leave", "fieldname": "on_leave_count", "fieldtype": "Int", "width": 100},
#         {"label": "Absent", "fieldname": "absent_count", "fieldtype": "Int", "width": 100}
#     ]

#     data = []

#     if filters.get("from_date") and filters.get("to_date"):
#         attendance_data = get_attendance_data(filters.get("from_date"), filters.get("to_date"))
#         data = list(attendance_data)

#     return columns, data

# def get_attendance_data(from_date, to_date):
#     attendance_counts = defaultdict(int)
#     present_counts = defaultdict(int)
#     on_leave_counts = defaultdict(int)
#     absent_counts = defaultdict(int)

#     attendances = frappe.get_all("Attendance", filters={"attendance_date": ["between", (from_date, to_date)]}, fields=["branch", "status", "employee"])
#     for attendance in attendances:
#         branch = attendance.get("branch")
#         status = attendance.get("status")
#         attendance_counts[branch] += 1
#         if status == "Present":
#             present_counts[branch] += 1
#         elif status == "On Leave":
#             on_leave_counts[branch] += 1
#         elif status == "Absent":
#             absent_counts[branch] += 1

#     data = []
#     for branch in attendance_counts.keys():
#         data.append({
#             "branch": branch,
#             "total_attendance_count": attendance_counts[branch],
#             "present_count": present_counts[branch],
#             "on_leave_count": on_leave_counts[branch],
#             "absent_count": absent_counts[branch]
#         })

#     return data


# def execute(filters=None):
#     columns = [
#         {"label": "Employee", "fieldname": "employee", "fieldtype": "Link", "options": "Employee", "width": 150},
#         {"label": "Date", "fieldname": "attendance_date", "fieldtype": "Date", "width": 100},
#         {"label": "Status", "fieldname": "status", "fieldtype": "Data", "width": 100},
#         {"label": "Branch", "fieldname": "branch", "fieldtype": "Link", "options": "Branch", "width": 150}
#     ]

#     data = []

#     if filters.get("from_date") and filters.get("to_date"):
#         attendances = frappe.get_all("Attendance", filters={"attendance_date": ["between", (filters.get("from_date"), filters.get("to_date"))]}, fields=["employee", "attendance_date", "status", "branch"])
#         data = attendances

#     return columns, data

