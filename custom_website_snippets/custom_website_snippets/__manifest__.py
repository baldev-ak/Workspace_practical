# -*- encoding: utf-8 -*-
{
    'name': 'Custom Website Snippets',
    'category': 'Website/Website',
    'summary': 'Custom Snippet',
    'version': '15.0.1.0.0',
    'description': "",
    'depends': [
        'web',
        'web_editor',
    ],
    'installable': True,
    'data': [
        'views/snippets/custom_snippets.xml',
        'views/snippets/custom_snippets_template.xml',
    ],
    'application': True,

    'assets': {
        'web.assets_frontend': [
            'custom_website_snippets/static/src/css/login_page.css',
        ],
    },
    'license': 'LGPL-3',
}
