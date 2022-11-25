# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'Goals website',
    'version' : '1.0',
    'summary': 'Goals website',
    'sequence': 0,
    'description': """Goals website""",
    'category': 'Extra Tools',
    'website': 'https://www.odoo.com/app/invoicing',
    'images' : [],
    'depends' : ['website'],
    'data': [
        # 'security/ir.model.access.csv',
        'views/goals_template.xml',
    ],
    'assets':{
    'web.assets_frontend': [
            'webpage/static/src/css/design.css',
            ]
    },
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
