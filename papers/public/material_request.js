frappe.ui.form.on('Material Request', {
    refresh:function(frm) {
       
        frm.set_query('address', function(doc) {
            if(doc.customer){
            return {
                query: 'frappe.contacts.doctype.address.address.address_query',
                filters: {
                    link_doctype: 'Customer',
                    link_name: doc.customer
                }
            };
        }
        })
    },
    material_request_type:function(frm){
        if(frm.doc.address) {
            frm.set_value("address", "")
            frm.set_value("dispatch_address", "")
           
        }
        if(frm.doc.customer) {
            frm.set_value("customer", "")
        }
    },
  
    address:function(frm) {
		if(frm.doc.address) {
			frappe.call({
				method: "frappe.contacts.doctype.address.address.get_address_display",
				args: {"address_dict": frm.doc.address },
				callback: function(r) {
					if(r.message) {
						me.frm.set_value("dispatch_address", r.message)
					}
				}
			})
		} else {
			this.frm.set_value("dispatch_address", "");
		}
	}
    
});