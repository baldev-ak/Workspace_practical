# -*- coding: utf-8 -*-

from odoo import http
from odoo.http import request


class Sales(http.Controller):

    @http.route('/college/webstudent', type='http', auth='user',
                website=True)
    def college_webstudent(self, **kw):
        """Function to get & store data in college_management.
        :return: record set"""
        if kw:
            request.env['res.partner'].sudo().create(kw)

        return request.render("custom_website_snippets.student_thankyou_page", {})

