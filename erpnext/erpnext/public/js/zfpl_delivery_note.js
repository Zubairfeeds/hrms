// frappe.ui.form.on('Delivery Note Item', {
// 	refresh(frm) {
		
// 	}
// })
frappe.ui.form.on('Delivery Note', {
    refresh: function(frm) {
        frm.doc.items.forEach(function(item) {
            item.price_list_amount = item.qty * item.price_list_rate;
            item.gross_discount_amount = item.qty * item.discount_amount;
        });
        // Refresh the child table to reflect the calculated values
        frm.refresh_field('items');
        console.log("DN")
    }
});


frappe.ui.form.on("Delivery Note Item",
    "price_list_rate", function(frm, cdt, cdn) 
{ 
    var d = locals[cdt][cdn];
    frappe.model.set_value(d.doctype, d.name, "price_list_amount", d.qty * d.price_list_rate ); 

    
});
frappe.ui.form.on("Delivery Note Item",
    "qty", function(frm, cdt, cdn) 
{
    var d = locals[cdt][cdn];
    frappe.model.set_value(d.doctype, d.name, "price_list_amount", d.qty * d.price_list_rate ); 

    
});

frappe.ui.form.on("Delivery Note Item",
    "qty", function(frm, cdt, cdn) 
{ 
    var d = locals[cdt][cdn];
    frappe.model.set_value(d.doctype, d.name, "gross_discount_amount", d.qty * d.discount_amount ); 

    
});
frappe.ui.form.on("Delivery Note Item",
    "item_code", function(frm, cdt, cdn) 
{ 
    var d = locals[cdt][cdn];
    frappe.model.set_value(d.doctype, d.name, "gross_discount_amount", d.qty * d.discount_amount ); 

    
});
 