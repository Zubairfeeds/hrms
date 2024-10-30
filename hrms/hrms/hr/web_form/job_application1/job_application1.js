//frappe.ready(function() {
// bind events here
//})

frappe.ready(function () {
    frappe.web_form.after_load = function () {
        var applyButton = $('<button>Apply Now</button>');
        applyButton.attr('id', 'applyNowButton');
        $('.web-form-footer').append(applyButton);

        // Bind a click event to the Apply Now button
        applyButton.on('click', function () {
            frappe.msgprint('Apply Now clicked!');
        });
    };
});


