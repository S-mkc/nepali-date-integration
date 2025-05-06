frappe.ui.form.on('Purchase Invoice', {
    refresh: function(frm){
        if(frm.is_new()){
            if (frm.doc.posting_date) {
                frm.trigger('posting_date');
            }
        }
        frm.set_df_property('nepali_date', 'hidden', 1);
    },
    posting_date(frm){
        frappe.model.set_value(frm.doctype, frm.docname, "nepali_date", NepaliFunctions.AD2BS(frm.doc.posting_date.split(" ")[0], "YYYY-MM-DD", "YYYY-MM-DD")); 
    }
});