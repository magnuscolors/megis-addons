# -*- coding: utf-8 -*-
from openupgradelib import openupgrade

from openerp.modules.registry import RegistryManager
from openerp import SUPERUSER_ID

#
#
# @openupgrade.migrate()
# def migrate(cr, version):
#
#     pool = RegistryManager.get(cr.dbname)
#     pool['ir.module.module'].update_list(cr, SUPERUSER_ID, [])
#
#     # Install alternate OCA module:
#     cr.execute("""
#         UPDATE ir_module_module set state = 'to install'
#         WHERE name = 'account_invoice_supplier_ref_unique';
#     """)
#
#
