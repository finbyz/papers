frappe.ui.form.on('Sales Order Item', {
 
    calculate:function(frm,cdt,cdn){
        let doc =locals[cdt][cdn];
        if(doc.qty){
           let rate = ((doc.rate_per_kg*doc.total_weight)/doc.qty)
        frappe.model.set_value(cdt, cdn, 'rate', rate)
        }
    },
});
       

    
