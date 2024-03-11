frappe.ui.form.on("Enquiry", { 
    customer: function (frm) {
        if (frm.doc.customer) {
            frappe.call({
                method:"ins.custom_script.enquiry.get_address_display",
                args: {
                    party: frm.doc.customer
                },
                callback: function(response) {
                    var address = response.message
                    console.log(address)
                    if (!response.exc) {

                        frm.set_value("customer_address", address.customer_address);
                        frm.set_value("address_display", address.address_display);
                
                    }
                }
            })
        }
        if (frm.doc.customer) {
            frm.fields_dict.customer_address.get_query = function (doc, cdt, cdn) {
                var d = locals[cdt][cdn];
                    console.log(d)
                return {
                    filters: {
                        "link_doctype": "Customer",
                        "link_name": d.customer
                    }
                };
            };
        } 
    
    },
    customer_address:function(frm){
        if (frm.doc.customer_address){
            frappe.call({
                method: "frappe.client.get",
                args: {
                    doctype: "Address",
                    name: frm.doc.customer_address,
                },
                callback: function(response) {
                    if (response.message){
                        var address = response.message;
                        console.log(address)
                        var custom_address_display = '';
                        if (address.address_line1) custom_address_display += address.address_line1 + '\n';
                        if (address.address_line2) custom_address_display += address.address_line2 + '\n';
                        if (address.city) custom_address_display += address.city + '\n';
                        if (address.state) custom_address_display += address.state + '\n';
                        if (address.pincode) custom_address_display += address.pincode + '\n';
                        if (address.country) custom_address_display += address.country + '\n';
                        if (address.email_id) custom_address_display += address.email_id + '\n';
                        if (address.phone) custom_address_display += address.phone;

                        // Use cur_frm.set_value to update the field
                        frm.set_value('address_display', custom_address_display);
                    }
                    console.log(response)
                }
            })

        }

    },

    lead: async function (frm) {
        let lead = await frappe.db.get_doc('Lead', frm.doc.lead);
        frm.set_value('probability', lead.custom_probability);
    },
})
