from odoo import api, fields, models, _
from datetime import date


class SaleOrder(models.Model):
    _inherit = "sale.order"

    order_lines = fields.Integer(
        string="Lines", compute="compute_line", default=0)
    # state = fields.Selection(selection_add=[
    #     ('draft', 'Quotation'),
    #     ('awaiting_approval', 'Awaiting Approval'),
    #     ('sent', 'Quotation Sent'),
    # ], string='Status', default='draft')

    @api.depends('order_line')
    def compute_line(self):
        for rec in self:
            lines = len(rec.order_line.ids)

        self.order_lines = lines

    @api.model
    def create(self, vals):
        # print("====================self", self)
        res = super(SaleOrder, self).create(vals)
        print("====================res", res.amount_total)
        return res

    def action_products_display(self):
        stock = self.env['stock.picking'].search(
            [('sale_id', '=', self.id), ('state', '!=', 'cancel')])

        action_id = self.env.ref('Motivation.product_wizard_view')
        product_list = []
        for rec in stock:
            for record in rec.move_ids_without_package:
                product_list.append(record.product_id.id)

        ctx = {
            'product_id': product_list,
            'sale_id': self.id
        }

        return {
            'type': 'ir.actions.act_window',
            'res_model': 'products.wizard',
            'view_mode': 'form',
            'name': 'Product wizard',
            'target': 'new',
            'view_id': action_id.id,
            'context': ctx
        }

    def btn_order_lines(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Order Lines',
            'view_mode': 'tree',
            'res_model': 'product.product',
            'domain': [('id', '=', self.order_line.product_id.ids)],
            'context': "{'create': False}"
        }
