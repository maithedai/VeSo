from odoo import models, fields, api
from datetime import datetime, date, timedelta


class LotCustomer(models.Model):
    _name = "lot.customer"
    # _inherits = {'res.partner': 'partner_id'}

    name = fields.Char(string='Họ tên')
    gender = fields.Selection(
        string='Giới tính',
        selection=[('female', 'Nam'), ('male', 'Nữ')])
    phone = fields.Char("Số điện thoại")
    address = fields.Char("Địa chỉ")
    unit_price = fields.Float("Đơn giá(%)")
    status = fields.Selection(
        string='Trạng thái',
        selection=[('active', 'Hoạt động'), ('block', 'Khóa')], default='active')
    note = fields.Char('Ghi chú')
    plan = fields.Selection(
        string='Kế hoạch lãnh',
        selection=[('0', 'Lãnh ngày hiện tại'),
                   ('1', 'Lãnh trước 1 ngày'),
                   ('2', 'Lãnh trước 2 ngày'),
                   ('3', 'Lãnh trước 3 ngày')], default='0')

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
