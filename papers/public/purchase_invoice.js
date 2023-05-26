

frappe.ui.form.on('Purchase Invoice Item', {
	calculate:function(frm,cdt,cdn){
		let doc =locals[cdt][cdn];
		if(doc.qty){
		   let rate = ((doc.rate_per_kg*doc.total_weight)/doc.qty)
		frappe.model.set_value(cdt, cdn, 'rate', rate)
		}
		if(doc.invoice_amount){
			let rate = ((doc.invoice_amount)/doc.qty)
			frappe.model.set_value(cdt,cdn,"amount",frm.doc.invoice_amount)
		frappe.model.set_value(cdt, cdn, 'rate', rate)
		}
	},
   
	
}
);
	