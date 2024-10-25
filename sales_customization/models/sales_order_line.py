from odoo import models, fields

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    testing = fields.Char(string='HS Code')
    launch_date = fields.Date(string='Launch Date', related='product_id.product_tmpl_id.launch_date', readonly=True)

    # launch_date = fields.Date(
    #     string="Launch Date",
    #     related='product_id.product_tmpl_id.launch_date',
    #     readonly=True
    # )
