#-*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2015-today Magnus www.magnus.nl
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

from openerp.addons.base_status.base_stage import base_stage
import crm
from datetime import datetime
from operator import itemgetter
from openerp.osv import fields, osv, orm
import openerp.addons.decimal_precision as dp
import time
from openerp import SUPERUSER_ID
from openerp import tools
from openerp.tools.translate import _
from openerp.tools import html2plaintext

from base.res.res_partner import format_address


class crm_lead(base_stage, format_address, osv.osv):
    """ Inherits crm_lead and adds tph_revenue_line O2M object to create time-phased backlog"""
    _inherit = 'crm.lead'

    _columns = {
        'tph_revenue_line': fields.one2many('crm.lead.tph.revenue.line', 'lead_id', 'Revenue Lines', readonly=False, states={'draft':[('readonly',False)]}),
        'tph_date_start': fields.date('Start Date', required=True, readonly=0),
        'tph_date_end': fields.date('End Date', required=True, readonly=0),
        'probability': fields.float('Success Rate (%)',group_operator="avg", track_visibility='always'),
    }


 
class crm_lead_tph_revenue_line(orm.Model):
    _name = "crm.lead.tph.revenue.line"
    _description = "Period Revenue Line"
    _order = "lead_id,id"
    _columns = {
        'period_id': fields.many2one('account.period', 'Period', required=True,),
        'nr_of_days': fields.integer('Number of Days in Period'),
        'period_amount': fields.float('Amount in Period', digits_compute=dp.get_precision('Account')),
        'lead_id': fields.many2one('crm.lead', 'Lead Reference', ondelete='cascade', select=True),
        'probability': fields.related('lead_id', 'probability', type="float", string="probability",
                readonly=True),
    }