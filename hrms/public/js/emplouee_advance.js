
frappe.ui.form.on('Employee Advance', {
    setup: function(frm) {
        frm.set_query("employee", function() {
            if (frm.doc.advance_type === 'Salary Advance') {
                return {
                    filters: {
                        employment_type: 'Full-time'
                    }
                };
            } else {
                return {};
            }
        });
    },
    advance_type: function(frm) {
        // Trigger the query refresh when advance_type changes
        frm.set_query("employee", function() {
            if (frm.doc.advance_type === 'Salary Advance') {
                return {
                    filters: {
                        employment_type: 'Full-time'
                    }
                };
            } else {
                return {};
            }
        });
    }
});