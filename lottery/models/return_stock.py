from odoo import models, fields, api
from datetime import datetime, date, timedelta


class ReturnStock(models.TransientModel):
    _name = "return.stock"

    customer_ids_2 = fields.One2many('lot.customer', compute='_compute_customer_ids')
    customer_ids_3 = fields.One2many('lot.customer', compute='_compute_customer_ids')
    customer_ids_4 = fields.One2many('lot.customer', compute='_compute_customer_ids')
    customer_ids_5 = fields.One2many('lot.customer', compute='_compute_customer_ids')
    customer_ids_6 = fields.One2many('lot.customer', compute='_compute_customer_ids')
    customer_ids_7 = fields.One2many('lot.customer', compute='_compute_customer_ids')
    customer_ids_cn = fields.One2many('lot.customer', compute='_compute_customer_ids')
    tele_ids_2 = fields.One2many('lot.tele', compute='_compute_tele_ids')
    tele_ids_3 = fields.One2many('lot.tele', compute='_compute_tele_ids')
    tele_ids_4 = fields.One2many('lot.tele', compute='_compute_tele_ids')
    tele_ids_5 = fields.One2many('lot.tele', compute='_compute_tele_ids')
    tele_ids_6 = fields.One2many('lot.tele', compute='_compute_tele_ids')
    tele_ids_7 = fields.One2many('lot.tele', compute='_compute_tele_ids')
    tele_ids_cn = fields.One2many('lot.tele', compute='_compute_tele_ids')
    date = fields.Date(default=fields.Date.context_today)
    weekday = fields.Selection(
        selection=[('0', '2'),
                   ('1', '3'),
                   ('2', '4'),
                   ('3', '5'),
                   ('4', '6'),
                   ('5', '7'),
                   ('6', 'cn')], compute='_compute_weekday')

    @api.depends('date')
    def _compute_customer_ids(self):
        for item in self:
            item.customer_ids_2 = self.env['lot.customer'].search([])
            item.customer_ids_3 = self.env['lot.customer'].search([])
            item.customer_ids_4 = self.env['lot.customer'].search([])
            item.customer_ids_5 = self.env['lot.customer'].search([])
            item.customer_ids_6 = self.env['lot.customer'].search([])
            item.customer_ids_7 = self.env['lot.customer'].search([])
            item.customer_ids_cn = self.env['lot.customer'].search([])

    @api.depends('date')
    def _compute_tele_ids(self):
        for item in self:
            item.tele_ids_2 = self.env['lot.tele'].search([])
            item.tele_ids_3 = self.env['lot.tele'].search([])
            item.tele_ids_4 = self.env['lot.tele'].search([])
            item.tele_ids_5 = self.env['lot.tele'].search([])
            item.tele_ids_6 = self.env['lot.tele'].search([])
            item.tele_ids_7 = self.env['lot.tele'].search([])
            item.tele_ids_cn = self.env['lot.tele'].search([])

    @api.depends('date')
    def _compute_weekday(self):
        for item in self:
            item.weekday = str(item.date.weekday())


class LotTele(models.Model):
    _name = "lot.tele"

    name = fields.Char('Đài')
    hcm_2 = fields.Integer('TP HCM')
    dt_2 = fields.Integer('ĐT')
    cm_2 = fields.Integer('CM')
    bl_3 = fields.Integer('BL')
    bt_3 = fields.Integer('BT')
    vt_3 = fields.Integer('VT')
    st_4 = fields.Integer('ST')
    ct_4 = fields.Integer('ĐN')
    dn_4 = fields.Integer('VT')
    tn_5 = fields.Integer('TN')
    ag_5 = fields.Integer('AG')
    bth_5 = fields.Integer('BTH')
    bd_6 = fields.Integer('BD')
    tv_6 = fields.Integer('TV')
    vl_6 = fields.Integer('VL')
    hcm_7 = fields.Integer('TP HCM')
    la_7 = fields.Integer('LA')
    bp_7 = fields.Integer('BP')
    hg_7 = fields.Integer('HG')
    kg_cn = fields.Integer('KG')
    dl_cn = fields.Integer('ĐL')
    tg_cn = fields.Integer('TG')