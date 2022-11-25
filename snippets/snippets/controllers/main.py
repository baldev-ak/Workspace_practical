from odoo import http
from odoo.http import request
import base64

class Main(http.Controller):
    @http.route('/create_user', type='http', auth="public", website=True)
    def Snippets(self,**kw):
        # lead = request.env['crm.lead'].search([])
        print("===============]",kw.get('image_1920'))
        image = kw.get('image_1920')
        imageBase64 = base64.b64encode(image.read())
        # print("===============image",imageBase64)
        values = {
        'name': kw.get('name'),
        'email': kw.get('email'),
        'website': kw.get('website'),
        'phone': kw.get('phone'),
        'image_1920': imageBase64
        }
        partner = request.env['res.partner'].create(values)

        Attachment = request.env['ir.attachment']
        file_name = kw.get('image_1920').filename
        # file = post.get('attachment')
        attachment_id = Attachment.create({
        'name': file_name,
        'type': 'binary',
        'datas': imageBase64,
        'res_model': partner._name,
        'res_id': partner.id
        })
        return request.render('website.contactus_thanks',{})
