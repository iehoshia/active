#! -*- coding: utf8 -*-
# This file is part of the sale_pos module for Tryton.
# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
# Josias

import datetime
from decimal import Decimal
from trytond.model import ModelView, fields, ModelSQL
from trytond.pool import PoolMeta, Pool
from trytond.pyson import Bool, Eval, Not
from datetime import timedelta, date 

__all__ = ['Asociacion']
__metaclass__ = PoolMeta

_ZERO = Decimal('0.0')
_YEAR = datetime.datetime.now().year

class Asociacion(ModelView, ModelSQL):
    'Asociacion'
    __name__ = 'disc.asociacion'
    name = fields.Char('Nombre')
    pastor = fields.Many2One('party.party','Pastor',
        domain=[('es_pastor', '=', True)])

    @classmethod
	def __setup__(cls):
		super(Asociacion, cls).__setup__()
		cls._order.insert(0, ('name', 'ASC'))
 