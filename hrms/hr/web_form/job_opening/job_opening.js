
// frappe.ready(function () {
//     var applyButton = $('<button>Apply Now</button>');

//     // Adding custom styling to the button (optional)
//     applyButton.css({
//         'background-color': '#007bff',
//         'color': '#fff',
//         'border': 'none',
//         'padding': '8px 16px',
//         'cursor': 'pointer',
//         'border-radius': '4px',
//         'position': 'absolute',
//         'bottom': '90px',
//         // 'top': '150px',
//         'right': '120px'
//     });

//     $('.web-form-header').append(applyButton);
//     // Event listener for Apply Now button click
//     applyButton.on('click', function () {
//         // Create a hidden form and submit it to the desired URL
//         var form = $('<form action="http://125.209.107.60/job-application1/new" method="POST"></form>');
//         $('body').append(form);
//         form.submit();
//     });
// });




// frappe.ready(function () {
//     var jobTitleField = $('[data-fieldname="job_title"]');
//     var designationField = $('[data-fieldname="designation"]');
//     var applyButton = $('<button>Apply Now</button>');

//     // Adding custom styling to the button (optional)
//     applyButton.css({
//         'background-color': '#007bff',
//         'color': '#fff',
//         'border': 'none',
//         'padding': '8px 16px',
//         'cursor': 'pointer',
//         'border-radius': '4px',
//         'position': 'absolute',
//         'bottom': '90px',
//         'right': '120px'
//     });

//     $('.web-form-header').append(applyButton);
//     applyButton.on('click', function () {
//         console.log("Job Title:", jobTitleField.val());
//         console.log("Designation:", designationField.val());

//         // Create a hidden form and submit it to the desired URL
//         var form = $('<form action="http://125.209.107.60/job-application1/new" method="GET"></form>');
//         form.append('<input type="hidden" name="job_title" value="' + jobTitleField.val() + '">');
//         form.append('<input type="hidden" name="designation" value="' + designationField.val() + '">');
//         $('body').append(form);
//         form.submit();
//     });
// });


// frappe.ready(function () {
//     var jobTitleField = $('[data-fieldname="job_title"]');
//     var designationField = $('[data-fieldname="designation"]');
//     var applyButton = $('<button>Apply Now</button>');

//     applyButton.css({
//         'background-color': '#007bff',
//         'color': '#fff',
//         'border': 'none',
//         'padding': '8px 16px',
//         'cursor': 'pointer',
//         'border-radius': '4px',
//         'position': 'absolute',
//         'bottom': '90px',
//         'right': '120px'
//     });

//     $('.web-form-header').append(applyButton);
//     applyButton.on('click', function () {
//         // Get the name and designation values from the Job Opening Form
//         var jobOpeningName = frappe.web_form.jb_opening;
//         var jobOpeningDesignation = frappe.web_form.get_value('designation');

//         // Set the name value to the job_title field on the Job Application Form
//         frappe.web_form.set_value('jb_opening', jobOpeningName);

//         // Set the designation value to the designation field on the Job Application Form
//         frappe.web_form.set_value('designation', jobOpeningDesignation);

//         // Log the values (optional)
//         console.log("Job Title (Job Opening Name):", jobOpeningName);
//         console.log("Designation (Job Opening Designation):", jobOpeningDesignation);

//         // Create a hidden form and submit it to the desired URL
//         var form = $('<form action="http://125.209.107.60/job-application1/new" method="GET"></form>');
//         form.append('<input type="hidden" name="job_title" value="' + jobOpeningName + '">');
//         form.append('<input type="hidden" name="designation" value="' + jobOpeningDesignation + '">');
//         $('body').append(form);
//         form.submit();
//     });
// });


frappe.ready(function () {
    var jobTitleField = $('[data-fieldname="job_title"]');
    var designationField = $('[data-fieldname="designation"]');
    var currency = $('[data-fieldname="currency"]');
    var applyButton = $('<button>Apply Now</button>');

    applyButton.css({
        'background-color': '#007bff',
        'color': '#fff',
        'border': 'none',
        'padding': '8px 16px',
        'cursor': 'pointer',
        'border-radius': '4px',
        'position': 'absolute',
        'bottom': '90px',
        'right': '120px'
    });

    $('.web-form-header').append(applyButton);
    applyButton.on('click', function () {
        // Get the name and designation values from the Job Opening Form
        var jobOpeningName = frappe.web_form.get_value('job_title');  // assuming 'jb_opening' is the fieldname for the job opening name
        var currency = frappe.web_form.get_value('currency');
        var jobOpeningDesignation = frappe.web_form.get_value('designation');

        // Set the name value to the job_title field on the Job Application Form
        frappe.web_form.set_value('job_title', jobOpeningName);

        frappe.web_form.set_value('currency', currency);

        // Set the designation value to the designation field on the Job Application Form
        frappe.web_form.set_value('designation', jobOpeningDesignation);

        // Log the values (optional)
        console.log("Job Title (Job Opening Name):", jobOpeningName);
        console.log("Designation (Job Opening Designation):", jobOpeningDesignation);

        // Create a hidden form and submit it to the desired URL
        var form = $('<form action="https://erp.zubairfeeds.com/job-application1/new" method="GET"></form>');
        form.append('<input type="hidden" name="job_title" value="' + jobOpeningName + '">');
        form.append('<input type="hidden" name="designation" value="' + jobOpeningDesignation + '">');
        form.append('<input type="hidden" name="currency" value="' + currency + '">');
        $('body').append(form);
        form.submit();
    });
});

