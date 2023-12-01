import frappe

@frappe.whitelist()
def get_prod_attr(partner):
    if partner != None:
        values = {'partner': partner}
        data = frappe.db.sql("""
            SELECT
                GROUP_CONCAT(DISTINCT lplp.loan_partner) AS loan_partners,
                GROUP_CONCAT(DISTINCT lc.charge_type) AS charge_type,
                lp.*

            FROM `tabLoan Product` lp
                INNER JOIN `tabLoan Product Loan Partner` lplp
                ON lp.name = lplp.parent
                JOIN `tabLoan Charges` lc
                ON lp.name = lc.parent
                
            WHERE lp.name = %(partner)s
            
        """, values=values, as_dict=1)
        return data