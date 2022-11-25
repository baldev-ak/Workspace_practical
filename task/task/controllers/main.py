# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import http, _
from odoo.http import request


class Main(http.Controller):
	http.route('/main',type='http', auth="public", website=True)

  