from odoo import models, fields, api
from datetime import datetime, date, timedelta


class ReturnStock(models.Model):
    _name = "return.stock"

    customer_ids = fields.One2many('lot.customer', 'return_stock_id')