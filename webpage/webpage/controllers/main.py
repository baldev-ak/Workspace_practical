from odoo import http
from odoo.http import request


class Goals(http.Controller):
	@http.route('/goals', type='http', auth="public", website=True)
	def Goals(self,**kwargs):
		# lead = request.env['crm.lead'].search([])
		return request.render('webpage.goals_templates',{})
