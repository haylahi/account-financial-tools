# -*- coding: utf-8 -*-
##############################################################################
#
#    Author Vincent Renaville/Joel Grand-Guillaume.
#    Copyright 2014 Camptocamp SA
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
##############################################################################

from openerp.osv import orm
from datetime import datetime


class AccountMoveLine(orm.Model):
    _inherit = 'account.move.line'

    def onchange_amount_currency(self, cr, uid, ids,
                                 amount_currency, currency_id,
                                 date, context=None):
        val = {}
        if not currency_id:
            return {'value': val}
        if not date:
            date = datetime.now().strftime('%Y-%m-%d')
        if amount_currency:
            currency_obj = self.pool['res.currency']
            company = self.pool['res.users'].browse(cr, uid, uid,
                                                    context=context).company_id
            company_currency = self.pool['res.company'].browse(
                cr, uid, company.id, context=context).currency_id
            if company_currency.id != currency_id:
                company_amount = currency_obj.compute(
                    cr, uid,
                    from_currency_id=currency_id,
                    to_currency_id=company_currency.id,
                    from_amount=amount_currency,
                    round=True, currency_rate_type_from=False,
                    currency_rate_type_to=False, context=context)
                if company_amount > 0.0:
                    val['debit'] = company_amount
                elif company_amount < 0.0:
                    val['credit'] = company_amount
        return {'value': val}
