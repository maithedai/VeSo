from odoo import models, fields, api
from datetime import datetime, date, timedelta


class ImportStock(models.TransientModel):
    _name = "import.stock"

    line_ids = fields.One2many('lot.tele.import', compute="_compute_line_ids")
    date = fields.Date(default=fields.Date.context_today)
    weekday = fields.Selection(
        selection=[('0', 't2'),
                   ('1', 't3'),
                   ('2', 't4'),
                   ('3', 't5'),
                   ('4', 't6'),
                   ('5', 't7'),
                   ('6', 'cn')], compute='_compute_weekday')

    @api.depends('date')
    def _compute_weekday(self):
        for item in self:
            item.weekday = str(item.date.weekday())

    @api.depends('date')
    def _compute_line_ids(self):
        for item in self:
            item.line_ids = self.env['lot.tele.import'].search([('weekday', '=', item.weekday)])


class LotTeleImport(models.Model):
    _name = 'lot.tele.import'

    name = fields.Char('Đài')
    num_im_com = fields.Integer('Số lượng nhập (Công ty)')
    num_im_pro = fields.Integer('Số lượng nhập (Liên tỉnh)')
    total = fields.Float('Tổng')
    weekday = fields.Selection(
        selection=[('0', 't2'),
                   ('1', 't3'),
                   ('2', 't4'),
                   ('3', 't5'),
                   ('4', 't6'),
                   ('5', 't7'),
                   ('6', 'cn')])

    @api.model
    def create(self, vals):
        print('11111111111111')
        return super(LotTeleImport, self).create(vals)

