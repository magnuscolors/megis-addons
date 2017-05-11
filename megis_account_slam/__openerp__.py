# -*- encoding: utf-8 -*-
##############################################################################
#
# Copyright (c) 2013 Eurogroup Consulting - Willem Hulshof - www.Eurogroupconsulting.nl
#
# WARNING: This program as such is intended to be used by professional
# programmers who take the whole responsability of assessing all potential
# consequences resulting from its eventual inadequacies and bugs.
# End users who are looking for a ready-to-use solution with commercial
# garantees and support are strongly adviced to contract a Free Software
# Service Company like Veritos.
#
# This program is Free Software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301  USA
#
##############################################################################
#
#   Deze module voegt twee velden toe aan account.analytic.line om de interface met slam
#   makkelijker te maken
##############################################################################
{
    'name' : 'megis_account_slam',
    'version' : '1.0',
    'category': 'integration',
    'description': """
This module adds two fields to account.analytic.line and one to account.journal
voor de interface naar slam.
=================================================================================
    """,
    'author'  : 'Eurogroup Consulting - Willem Hulshof',
    'website' : 'http://www.eurogroupconsulting.nl',
    'depends' : ['account',
                 'base_vat',
                 'base_iban',
                 # 'account_chart', -- deep
                 'analytic'
    ],
    'data' : ['account_slam_view.xml'],
    'demo' : [],
    'installable': True
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:

