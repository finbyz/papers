
frappe.ui.form.on('Purchase Order', {
    onload(frm){
        frm.set_query("shipping_address", function(frm) {
            return {
				filters: {
					is_your_company_address : 0
				}
			}
        });
    },

});



frappe.ui.form.on('Purchase Order Item', {
    calculate:function(frm,cdt,cdn){
        let doc =locals[cdt][cdn];
        if(doc.qty){
           let rate = ((doc.rate_per_kg*doc.total_weight)/doc.qty)
        frappe.model.set_value(cdt, cdn, 'rate', rate)
        }
    },
    
});
    