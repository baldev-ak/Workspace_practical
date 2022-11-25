# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'Motivation',
    'version' : '1.0',
    'summary': 'Motivation',
    'sequence': 0,
    'description': """Motivation""",
    'category': 'Extra Tools',
    'website': 'https://www.odoo.com',
    'depends' : ['hr','sale_management','sale', 'website'],
    'data': [
    # 'security/security.xml', #Practicing Groups and Record Rules
    'security/ir.model.access.csv',
    'data/game_seq.xml',
    'views/games_view.xml',
    'views/game_template_custom.xml',
    'views/inherit_sale_menu.xml',
    'wizard/products_view.xml',
    # 'report/game_report_template.xml', #Practicing Report
    # 'report/game_report.xml',
    
    ],
    'demo': [],
    'assets': {
        'web.assets_frontend': [
            'Motivation/static/src/js/events.js'
        ]
    },
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
