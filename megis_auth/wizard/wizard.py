# -*- coding: utf-8 -*-

from openerp import api, fields, models

import logging
_logger = logging.getLogger(__name__)

class MigrationFix(models.TransientModel):
    _name = 'wiz.migration.fix'

    @api.multi
    def recompute_InvoiceTotals(self):
        '''
            This method needs to be executed only once, after Migration.

        '''
        cr = self._cr
        InvObj = self.env['account.invoice']

        # From Odoo 7: Tax Application set to 'All' are mostly used in Supplier Invoice,
        # hence in Odoo 9 by default setting it to 'Purchase'.
        cr.execute("update account_tax set type_tax_use = 'purchase' where type_tax_use = 'none';")

        # cr.execute("select id from account_invoice order by id;")
        for i in cr.fetchall():
            inv = InvObj.browse(i[0])
            inv = InvObj.browse(i)

            _logger.info("Recomputing Invoice ______________________ # %s - [%s]"%(inv.id, str(inv.number)))

            Cancel = False
            if inv.state == 'cancel':
                Cancel  = True
                inv.action_cancel_draft()

            for ln in inv.invoice_line_ids:
                ln.write({'quantity': ln.quantity})
        _logger.info("______________ End of Computing _________________")