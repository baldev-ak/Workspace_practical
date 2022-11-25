# -*- coding: utf-8 -*-
from odoo import api, fields, models, _, tools
from odoo.osv import expression
from odoo.exceptions import UserError, ValidationError


class Task(models.Model):
    _name = "task.one"
    _description = "Task 1"
    _rec_name = "customer_id"

    customer_id = fields.Many2one(comodel_name="res.partner", string="Customer")
    state = fields.Selection([
        ('draft', 'Quotation'),
        ('sent', 'Quotation Sent'),
        ('sale', 'Sales Order'),
        ('cancel', 'Cancelled')], string='Status', default='draft')

    product_ids = fields.Many2many(comodel_name='product.product', string="Products")

    def action_create_sales(self):
        # print("----------------test", self)
        # print("----------------test\n", self.state)
        # print("----------------test\n", self.product_ids)

        for record in self:
            lines = []
            for rec in record.product_ids:
                lines.append((0, 0, {
                    'product_id': rec.id,
                }))
            sales = self.env['sale.order'].new({
                'partner_id': record.customer_id.id,
                'state': record.state,
                'order_line': lines
            })

            sales.onchange_partner_id()
            values = sales._convert_to_write(sales._cache)
            rec = self.env['sale.order'].create(values)
