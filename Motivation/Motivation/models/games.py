from odoo import api, fields, models, _
from datetime import date
from odoo.exceptions import UserError, ValidationError


class Games(models.Model):
    _name = "game.game"
    _description = "Games"

    name = fields.Char(string="Name")
    game_ref_no = fields.Char(string='Game Reference', required=True,
                              readonly=True, copy=False, default=lambda self: _('New'))
    status = fields.Selection([('online', 'Online'), ('offline', 'Offline')])
    launch_date = fields.Date(string='Launch Date')
    employee_id = fields.Many2one(string="employee",
                                  comodel_name="hr.employee")

    @api.model
    def create(self, vals):
        if vals.get('game_ref_no', _('New')) == _('New'):
            vals['game_ref_no'] = self.env['ir.sequence'].next_by_code(
                'game.game') or _('New')

        res = super(Games, self).create(vals)
        return res

    # def write(self,vals):
    #     res = super(Games, self).write(vals)

    #     print("______________________\n\n",res)
    # return res


class Employees(models.Model):
    _inherit = 'hr.employee'

    def name_get(self):
        result = []
        for rec in self:
            result.append((rec.id, '%s - %s' % (rec.name, rec.job_title)))
        return result

    @api.model
    def _name_search(self, name, args=None, operator='ilike', limit=100, name_get_uid=None):
        args = list(args or [])
        # if not (name == '' and operator == 'ilike'):
        if name:
            args += ['|', '|', ('name', operator, name), ('department_id.name',
                                                          operator, name), ('work_email', operator, name)]

        return self._search(args, limit=limit, access_rights_uid=name_get_uid)
