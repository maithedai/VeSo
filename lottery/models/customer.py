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

    r_hcm_2 = fields.Integer('TP HCM')
    r_dt_2 = fields.Integer('ĐT')
    r_cm_2 = fields.Integer('CM')
    r_bl_3 = fields.Integer('BL')
    r_bt_3 = fields.Integer('BT')
    r_vt_3 = fields.Integer('VT')
    r_st_4 = fields.Integer('ST')
    r_ct_4 = fields.Integer('ĐN')
    r_dn_4 = fields.Integer('VT')
    r_tn_5 = fields.Integer('TN')
    r_ag_5 = fields.Integer('AG')
    r_bth_5 = fields.Integer('BTH')
    r_bd_6 = fields.Integer('BD')
    r_tv_6 = fields.Integer('TV')
    r_vl_6 = fields.Integer('VL')
    r_hcm_7 = fields.Integer('TP HCM')
    r_la_7 = fields.Integer('LA')
    r_bp_7 = fields.Integer('BP')
    r_hg_7 = fields.Integer('HG')
    r_kg_cn = fields.Integer('KG')
    r_dl_cn = fields.Integer('ĐL')
    r_tg_cn = fields.Integer('TG')

    p_hcm_2 = fields.Integer('TP HCM', compute="_compute_percent_p")
    p_dt_2 = fields.Integer('ĐT', compute="_compute_percent_p")
    p_cm_2 = fields.Integer('CM', compute="_compute_percent_p")
    p_bl_3 = fields.Integer('BL', compute="_compute_percent_p")
    p_bt_3 = fields.Integer('BT', compute="_compute_percent_p")
    p_vt_3 = fields.Integer('VT', compute="_compute_percent_p")
    p_st_4 = fields.Integer('ST', compute="_compute_percent_p")
    p_ct_4 = fields.Integer('ĐN', compute="_compute_percent_p")
    p_dn_4 = fields.Integer('VT', compute="_compute_percent_p")
    p_tn_5 = fields.Integer('TN', compute="_compute_percent_p")
    p_ag_5 = fields.Integer('AG', compute="_compute_percent_p")
    p_bth_5 = fields.Integer('BTH', compute="_compute_percent_p")
    p_bd_6 = fields.Integer('BD', compute="_compute_percent_p")
    p_tv_6 = fields.Integer('TV', compute="_compute_percent_p")
    p_vl_6 = fields.Integer('VL', compute="_compute_percent_p")
    p_hcm_7 = fields.Integer('TP HCM', compute="_compute_percent_p")
    p_la_7 = fields.Integer('LA', compute="_compute_percent_p")
    p_bp_7 = fields.Integer('BP', compute="_compute_percent_p")
    p_hg_7 = fields.Integer('HG', compute="_compute_percent_p")
    p_kg_cn = fields.Integer('KG', compute="_compute_percent_p")
    p_dl_cn = fields.Integer('ĐL', compute="_compute_percent_p")
    p_tg_cn = fields.Integer('TG', compute="_compute_percent_p")

    percent = fields.Float("%")
    sum_return = fields.Integer("Tổng trả")
    consume = fields.Integer("Tiêu thụ")
    ticket_receive = fields.Integer("Lượng vé lãnh")
    du_thieu = fields.Integer('Dư thiếu')
    revenues = fields.Float('Tiền thu')

    @api.depends('r_hcm_2', 'hcm_2',
                 'r_dt_2', 'dt_2',
                 'r_cm_2', 'cm_2',
                 'r_bl_3', 'bl_3',
                 'r_bt_3', 'bt_3',
                 'r_vt_3', 'vt_3',
                 'r_st_4', 'st_4',
                 'r_ct_4', 'ct_4',
                 'r_dn_4', 'dn_4',
                 'r_tn_5', 'tn_5',
                 'r_ag_5', 'ag_5',
                 'r_bth_5', 'bth_5',
                 'r_bd_6', 'bd_6',
                 'r_tv_6', 'tv_6',
                 'r_vl_6', 'vl_6',
                 'r_hcm_7', 'hcm_7',
                 'r_la_7', 'la_7',
                 'r_bp_7', 'bp_7',
                 'r_hg_7', 'hg_7',
                 'r_kg_cn', 'kg_cn',
                 'r_dl_cn', 'dl_cn',
                 'r_tg_cn', 'tg_cn',
                 )
    def _compute_percent_p(self):
        for r in self:
            r.p_hcm_2 = r.r_hcm_2 / r.hcm_2 * 100 if r.hcm_2 > 0 else 0
            r.p_dt_2 = r.r_dt_2 / r.dt_2 * 100 if r.dt_2 > 0 else 0
            r.p_cm_2 = r.r_cm_2 / r.cm_2 * 100 if r.cm_2 > 0 else 0
            r.p_bl_3 = r.r_bl_3 / r.bl_3 * 100 if r.bl_3 > 0 else 0
            r.p_bt_3 = r.r_bt_3 / r.bt_3 * 100 if r.bt_3 > 0 else 0
            r.p_vt_3 = r.r_vt_3 / r.vt_3 * 100 if r.vt_3 > 0 else 0
            r.p_st_4 = r.r_st_4 / r.st_4 * 100 if r.st_4 > 0 else 0
            r.p_ct_4 = r.r_ct_4 / r.ct_4 * 100 if r.ct_4 > 0 else 0
            r.p_dn_4 = r.r_dn_4 / r.dn_4 * 100 if r.dn_4 > 0 else 0
            r.p_tn_5 = r.r_tn_5 / r.tn_5 * 100 if r.tn_5 > 0 else 0
            r.p_ag_5 = r.r_ag_5 / r.ag_5 * 100 if r.ag_5 > 0 else 0
            r.p_bth_5 = r.r_bth_5 / r.bth_5 * 100 if r.bth_5 > 0 else 0
            r.p_bd_6 = r.r_bd_6 / r.bd_6 * 100 if r.bd_6 > 0 else 0
            r.p_tv_6 = r.r_tv_6 / r.tv_6 * 100 if r.tv_6 > 0 else 0
            r.p_vl_6 = r.r_vl_6 / r.vl_6 * 100 if r.vl_6 > 0 else 0
            r.p_hcm_7 = r.r_hcm_7 / r.hcm_7 * 100 if r.hcm_7 > 0 else 0
            r.p_la_7 = r.r_la_7 / r.la_7 * 100 if r.la_7 > 0 else 0
            r.p_bp_7 = r.r_bp_7 / r.bp_7 * 100 if r.bp_7 > 0 else 0
            r.p_hg_7 = r.r_hg_7 / r.hg_7 * 100 if r.hg_7 > 0 else 0
            r.p_kg_cn = r.r_kg_cn / r.kg_cn * 100 if r.kg_cn > 0 else 0
            r.p_dl_cn = r.r_dl_cn / r.dl_cn * 100 if r.dl_cn > 0 else 0
            r.p_tg_cn = r.r_tg_cn / r.tg_cn * 100 if r.tg_cn > 0 else 0

    def action_edit(self):
        return {
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'res_model': 'lot.customer',
            'res_id': self.id,
            'views': [(self.env.ref("lottery.lot_customer_form").id, 'form')],
            'target': 'new',
        }

    def action_delete(self):
        self.unlink()
