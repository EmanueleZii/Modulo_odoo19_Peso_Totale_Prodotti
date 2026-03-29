from odoo import models, fields, api


class PurchaseOrder(models.Model):
    _inherit='purchase.order'

    weight_total = fields.Float(string='peso totale',compute='_compute_weight_total', store=True)

    @api.depends('order_line.product_qty', 'order_line.product_id.weight')
    def _compute_weight_total(self):
        for rec in self:
            total = sum(line.product_qty * (line.product_id.weight or 0) for line in rec.order_line)
            rec.weight_total = total