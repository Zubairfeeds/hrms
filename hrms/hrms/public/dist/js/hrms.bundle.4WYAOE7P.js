(()=>{frappe.templates.employees_with_unmarked_attendance=`{% if data.length %}

<div class="form-message yellow">
	<div>
		{{
			__(
				"Attendance is pending for these employees between the selected payroll dates. Mark attendance to proceed. Refer {0} for details.",
				["<a href='/app/query-report/Monthly%20Attendance%20Sheet'>Monthly Attendance Sheet</a>"]
			)
		}}
	</div>
</div>

<table class="table table-bordered small">
	<thead>
		<tr>
			<th style="width: 14%" class="text-left">{{ __("Employee") }}</th>
			<th style="width: 16%" class="text-left">{{ __("Employee Name") }}</th>
			<th style="width: 12%" class="text-left">{{ __("Unmarked Days") }}</th>
		</tr>
	</thead>
	<tbody>
		{% for item in data %}
			<tr>
				<td class="text-left"> {{ item.employee }} </td>
				<td class="text-left"> {{ item.employee_name }} </td>
				<td class="text-left"> {{ item.unmarked_days }} </td>
			</tr>
		{% } %}
	</tbody>
</table>

{% } else { %}

<div class="form-message green">
	<div>{{ __("Attendance has been marked for all the employees between the selected payroll dates.") }}</div>
</div>

{% } %}`;frappe.provide("hrms");frappe.provide("hrms.utils");$.extend(hrms,{proceed_save_with_reminders_frequency_change:()=>{frappe.ui.hide_open_dialog(),frappe.call({method:"hrms.hr.doctype.hr_settings.hr_settings.set_proceed_with_frequency_change",callback:()=>{cur_frm.save()}})},set_payroll_frequency_to_null:e=>{cint(e.doc.salary_slip_based_on_timesheet)&&e.set_value("payroll_frequency","")},get_current_employee:async e=>{var t,a;return(a=(t=await frappe.db.get_value("Employee",{user_id:frappe.session.user},"name"))==null?void 0:t.message)==null?void 0:a.name}});})();
//# sourceMappingURL=hrms.bundle.4WYAOE7P.js.map
