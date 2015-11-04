# -*- coding: utf-8 -*-
##############################################################################
#
#    Copyright (c) 2009 CamptoCamp. All rights reserved.
#    @author Nicolas Bessi
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

import logging

from datetime import datetime, time
from dateutil.relativedelta import relativedelta

from openerp import models, fields, api, _
from openerp import exceptions

from ..services.currency_getter import Currency_getter_factory
from openerp.addons.base_currency_rate_update.model import currency_rate_update

CH_ADMIN_supported_currency_array = [
    "AED", "ALL", "ARS", "AUD", "AZN", "BAM", "BDT", "BGN", "BHD", "BRL",
    "CAD", "CHF", "CLP", "CNY", "COP", "CRC", "CZK", "DKK", "DOP", "EGP",
    "ETB", "EUR", "GBP", "GTQ", "HKD", "HNL", "HRK", "HUF", "IDR", "ILS",
    "INR", "ISK", "JPY", "KES", "KHR", "KRW", "KWD", "KYD", "KZT", "LBP",
    "LKR", "LTL", "LVL", "LYD", "MAD", "MUR", "MXN", "MYR", "NGN", "NOK",
    "NZD", "OMR", "PAB", "PEN", "PHP", "PKR", "PLN", "QAR", "RON", "RSD",
    "RUB", "SAR", "SEK", "SGD", "THB", "TND", "TRY", "TWD", "TZS", "UAH",
    "USD", "UYU", "VEF", "VND", "ZAR"]

currency_rate_update.supported_currecies = {
    'CH_ADMIN_getter': CH_ADMIN_supported_currency_array,
    }


