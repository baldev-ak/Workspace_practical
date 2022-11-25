from odoo import api, fields, models, _
from datetime import date
from odoo.exceptions import UserError, ValidationError


class ProductsCustom(models.TransientModel):
    _name = "products.wizard"
    _description = "Products Wizard"

    product_ids = fields.One2many(
        string="Product", inverse_name="product_wiz_id", comodel_name='products.split.wizard')

    def default_get(self, vals):
        result = super(ProductsCustom, self).default_get(vals)

        products = self.env['product.product'].browse(
            self.env.context.get('product_id'))

        sale = self.env['sale.order'].browse(self.env.context.get('sale_id'))

        product_list = []
        for move_rec in sale.picking_ids.move_ids_without_package:
            line = (0, 0, {
                'product_id': move_rec.product_id,
                'split_id': move_rec
            })

            product_list.append(line)

        result.update({
            'product_ids': product_list
        })

        return result

    def action_submit_split(self):
        print("============", self.product_ids)


class Products(models.TransientModel):
    _name = "products.split.wizard"

    product_wiz_id = fields.Many2one(
        string="Product Wiz Id", comodel_name="products.wizard")
    product_id = fields.Many2one(
        string="Product", comodel_name="product.product")
    split_id = fields.Many2one(string="Move ID", comodel_name="stock.move")
    select_product = fields.Boolean(string="Check")
