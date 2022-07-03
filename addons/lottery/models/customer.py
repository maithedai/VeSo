from odoo import models, fields, api
from datetime import datetime, date, timedelta


class LotCustomer(models.Model):
    _name = "lot.customer"
    # _inherits = {'res.partner': 'partner_id'}

    name = fields.Char(string='Họ tên')
