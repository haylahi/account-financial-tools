# -*- coding: utf-8 -*-
##############################################################################
#
#    Author Vincent Renaville. Copyright 2013 Camptocamp SA
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
{"name": "Tax analysis",
 "version": "1.0",
 "depends": ["base", "account"],
 "author": "CamptoCamp SA",
 "category": 'Accounting & Finance',
 "description": """
Tax analysis view
=================

This add-on is a must if you want to be able to validate your VAT form.

Thanks to a new menu 'Accounting / Tax / Tax analysis'
you are able to group accounting entries by Taxes (VAT codes)
and/or financial accounts.

This way you will find easily differences you may see between
the OpenERP tax report and what you see in your books.""",
 "website": "http://www.camptocamp.com",
 "data": ["account_tax_analysis_view.xml"],
 'installable': False,
 "active": False,
 }
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
