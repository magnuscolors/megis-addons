# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2013 Eurogroup Consulting NL (<http://eurogroupconsulting.nl>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

# import time
# from lxml import etree
# import odoo.addons.decimal_precision as dp
# import odoo.exceptions

# from odoo.osv import orm
# from odoo.tools.translate import _

from odoo import models, fields, api


class AccountInvoice(models.Model):
    """ Inherits invoice and adds state "auth" to supplier invoice workflow """
    _inherit = 'account.invoice'

    state = fields.Selection([
            ('draft','Draft'),
            ('proforma','Pro-forma'),   
            ('proforma2','Pro-forma'),
            ('open','Open'),
            ('auth','Goedgekeurd'),
            ('paid','Paid'),
            ('cancel','Cancelled'),
            ],'Status', select=True, readonly=True, track_visibility='onchange',
            help=' * The \'Draft\' status is used when a user is encoding a new and unconfirmed Invoice. \
            \n* The \'Pro-forma\' when invoice is in Pro-forma status,invoice does not have an invoice number. \
            \n* The \'Goedgekeurd\' status is used when invoice is already posted, but not yet confirmed for payment. \
            \n* The \'Open\' status is used when user create invoice,a invoice number is generated.Its in open status till user does not pay invoice. \
            \n* The \'Paid\' status is set automatically when the invoice is paid. Its related journal entries may or may not be reconciled. \
            \n* The \'Cancelled\' status is used when user cancel invoice.')
    payment_term = fields.Many2one('account.payment.term', 'Payment Terms',readonly=True, states={'draft':[('readonly',False)]},
            help="If you use payment terms, the due date will be computed automatically at the generation "\
                "of accounting entries. If you keep the payment term and the due date empty, it means direct payment. "\
                "The payment term may compute several due dates, for example 50% now, 50% in one month.", groups="account.group_account_invoice")
    user_id = fields.Many2one('res.users', 'Salesperson', readonly=True, track_visibility='onchange', states={'draft':[('readonly',False)],'open':[('readonly',False)]})
    reference = fields.Char('Invoice Reference', size=64, help="The partner reference of this invoice.", groups="account.group_account_invoice")
    amount_to_pay = fields.Float(related='residual', string='Amount to be paid',
            help='The amount which should be paid at the current date.', groups="account.group_account_invoice")
        

    #Already in standard 10.0 because workflow was abandoned:
 #   @api.multi
 #   def invoice_validate(self):
 #       self.write({'state':'open'})
 #       return super(account_invoice, self).invoice_validate()

     #I think already correct in standard (WH)
#    @api.multi
#    def action_date_assign(self):
#        for inv in self:
#            # Here the onchange will automatically write to the database
#            if not inv.date_due:
#                inv._onchange_payment_term_date_invoice()
#        return True

    # -- ported from Odoo 8
    @api.multi
    def move_line_id_payment_get(self):
        # return the move line ids with the same account as the invoice self
        if not self.id:
            return []
        query = """ SELECT l.id
                    FROM account_move_line l, account_invoice i
                    WHERE i.id = %s AND l.move_id = i.move_id AND l.account_id = i.account_id
                """
        self._cr.execute(query, (self.id,))
        return [row[0] for row in self._cr.fetchall()]

    # -- ported from Odoo 8
    @api.multi
    def test_paid(self):
        # check whether all corresponding account move lines are reconciled
        line_ids = self.move_line_id_payment_get()

        if not line_ids:
            return False
        query = "SELECT reconciled FROM account_move_line WHERE id IN %s"
        self._cr.execute(query, (tuple(line_ids),))
        return all(row[0] for row in self._cr.fetchall())
