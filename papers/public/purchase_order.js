
frappe.ui.form.on('Purchase Order Item', {
    reverse_conversion_factor:function(frm,cdt,cdn){ 
        let doc =locals[cdt][cdn];
        
            if (doc.reverse_conversion_factor){
                let rate =1/doc.reverse_conversion_factor
                frappe.model.set_value(cdt, cdn, 'conversion_factor', rate.toPrecision(3))
            }
       
    },  
    stock_qty:function(frm,cdt,cdn){
        let doc =locals[cdt][cdn]
        if(doc.uom =="Kgs"){
            let qty = doc.stock_qty/doc.conversion_factor
            console.log(qty)
            frappe.model.set_value(cdt, cdn, 'qty', qty)
        }
    },
    
});
    