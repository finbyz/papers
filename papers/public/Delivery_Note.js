
frappe.ui.form.on('Delivery Note Item', {
    reverse_conversion_factor:function(frm,cdt,cdn){ 
        let doc =locals[cdt][cdn];
        
            if (doc.reverse_conversion_factor){
                let rate =1/doc.reverse_conversion_factor
                frappe.model.set_value(cdt, cdn, 'conversion_factor', rate.toPrecision(3))
            }
       
    },  
    stock_qty:function(frm,cdt,cdn){
        let doc =locals[cdt][cdn]
        console.log("start")
        if(doc.uom =="Kgs"){
            let qty = doc.stock_qty/doc.conversion_factor
            console.log(qty)
            frappe.model.set_value(cdt, cdn, 'qty', qty)
        }
    },
    stock_uom_rate:function(frm,cdt,cdn){ 
        let doc =locals[cdt][cdn];
            if (doc.uom =="Kgs"){
                let rate = ((doc.stock_qty*doc.stock_uom_rate)/doc.qty);
                frappe.model.set_value(cdt, cdn, 'rate', rate)
            }
       
    },
    
});
    