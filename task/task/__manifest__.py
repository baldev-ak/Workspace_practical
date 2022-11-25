# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'Task 1',
    'version' : '1.0',
    'summary': 'Task 1',
    'sequence': 0,
    'description': """Task 1""",
    'category': 'Extra Tools',
    'website': 'https://www.odoo.com/app/invoicing',
    'images' : [],
    'depends' : ['sale','sale_management'],
    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/task_view.xml',
        'views/server_action.xml',
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
