frappe.ui.form.on('Purchase Invoice', {
    refresh(frm) {
        if (frm.doc.custom_purchase_type == "Direct Purchase") {
            remove_columns(frm, ["item_code"],
                "items", 1, lock_child_table_grid = false
            );
            remove_columns(frm, ["expense_account"],
                "items", 0, lock_child_table_grid = false
            );
        }
        else{
            remove_columns(frm, ["item_code"],
                "items", 0, lock_child_table_grid = false
            );
            remove_columns(frm, ["expense_account"],
                "items", 1, lock_child_table_grid = false
            );
        }
    },
    custom_purchase_type: function (frm) {
        if (frm.doc.custom_purchase_type == "Direct Purchase") {
            remove_columns(frm, ["item_code"],
                "items", 1, lock_child_table_grid = false
            );
            remove_columns(frm, ["expense_account"],
                "items", 0, lock_child_table_grid = false
            );
            frm.doc.items = []
            frm.add_child("items",{
                "item_code": "Direct Purchase",
                "item_name": "Direct Purchase",
                "uom": "Nos"
            })
            frm.refresh_field("items")
        }
        else{
            frm.doc.items = []
            remove_columns(frm, ["item_code"],
                "items", 0, lock_child_table_grid = false
            );
            remove_columns(frm, ["expense_account"],
                "items", 1, lock_child_table_grid = false
            );
            frm.refresh_field("items")
        }
    }
})
frappe.ui.form.on('Purchase Invoice Item', {
	items_add(frm, cdt, cdn) {
		if (frm.doc.custom_purchase_type == "Direct Purchase") {
            let row = locals [cdt] [cdn]
            frappe.model.set_value("Purchase Invoice Item", row.name, "item_code", "Direct Purchase")
        }
	}
})
function remove_columns(frm, fields, table, hidden_field_value, lock_child_table_grid) {
    let grid = frm.get_field(table).grid;

    for (let field of fields) {
        grid.fields_map[field].hidden = hidden_field_value;
        grid.fields_map[field].reqd = hidden_field_value;
    }

    grid.visible_columns = undefined;
    grid.setup_visible_columns();

    grid.header_row.wrapper.remove();
    delete grid.header_row;
    grid.make_head();

    for (let row of grid.grid_rows) {
        if (row.open_form_button) {
            row.open_form_button.parent().remove();
            delete row.open_form_button;
        }

        for (let field in row.columns) {
            if (row.columns[field] !== undefined) {
                row.columns[field].remove();
            }
        }
        delete row.columns;
        row.columns = [];
        row.render_row();
    }
    if (lock_child_table_grid == true) {
        grid.cannot_add_rows = true;
        grid.cannot_delete_rows = true;
        grid.wrapper.find(".grid-remove-rows").hide();
        grid.wrapper.find(".grid-add-row").hide();
        grid.wrapper.find(".grid-remove-all-rows").hide();
    }
}