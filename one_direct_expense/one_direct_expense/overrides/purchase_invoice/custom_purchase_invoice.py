import frappe

from erpnext.accounts.doctype.purchase_invoice.purchase_invoice import PurchaseInvoice

class CustomPurchaseInvoice(PurchaseInvoice):
    def before_save(self):
        super().before_save()
        if self.custom_purchase_type == "Direct Purchase":
            for i in self.items:
                if not i.expense_account:
                    frappe.throw("Row {0}: Expense Account is mandatory when Purchase Type is Direct Expense".format(i.idx))