# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'Snippets',
    'version' : '1.0',
    'summary': 'Snippets',
    'sequence': 0,
    'description': """Snippets""",
    'category': 'Extra Tools',
    'website': 'https://www.odoo.com/app/invoicing',
    'images' : [],
    'depends' : ['website'],
    'data': [
        # 'security/ir.model.access.csv',
        'views/snippet.xml',
        'views/template.xml',
    ],
    'assets':{
    'web.assets_frontend': [
            'snippets/static/src/css/design.css',
            ]
    },
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
