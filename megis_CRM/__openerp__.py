# -*- coding: utf-8 -*-
##############################################################################
#
#    Copyright 2016 Magnus WH
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

{
    "name": "Magnus Account Relation System (MARS)",
    "version": "1.0",
    "author": "Magnus",
    "website": "https://www.magnus.nl",
    "category": "CRM",
    "depends": [
        "base",
        "crm",

    ],
    "summary": "Revenue Estimation Tool",
    "description": """
        This module adds functionality, that allocates estimated revenue to periods in the future times a probability%
    """,
    'images': [
    ],
    'data': [
    ],
    "init_xml": [
    ],
    "update_xml": [
        "megis_crm_lead.xml",
    ],
    'demo_xml': [
    ],
    'test': [
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
