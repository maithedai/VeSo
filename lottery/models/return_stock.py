from odoo import models, fields, api
from datetime import datetime, date, timedelta


class ReturnStock(models.Model):
    _name = "return.stock"

    customer_ids = fields.One2many('lot.customer', 'return_stock_id')
    tele_ids = fields.One2many('lot.tele', 'return_stock_id')
    date = fields.Date()


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

    return_stock_id = fields.Many2one('return.stock')