# -*- coding: utf-8 -*-
{
    'name': "aa_test",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.2',
    'price': 14.95,
    'currency': 'EUR',

    # any module necessary for this one to work correctly
    'depends': ['sale', 'purchase', 'custom_module_xyz', 'aa_test_two', 'sale_ebay', 'web_studio'],
    'services': [
      {
        'name': 'Extended support',
        'info': 'Extend the support/service on this app with an extra 60 days.',
        'price': 49.95,
        'currency': 'EUR',
      },
      {
        'name': 'Installation service',
        'info': 'We will install and configure the app for you / with you.',
        'price': 24.99,
        'currency': 'EUR',
      }
    ],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
