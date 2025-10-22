{
    'name': "bajukertas_helpdesk",

    'summary': "Helpdesk for customer design uploads",

    'description': """
Helpdesk for customer design uploads
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'mail', 'sale_management'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/helpdesk_ticket_views.xml',
        'views/sale_order_views.xml',
        # 'views/portal_templates.xml',
        # 'views/portal_login.xml',
        # 'views/portal_dashboard.xml',
        # 'views/portal_ticket_form.xml',
        # 'views/views.xml',
        # 'views/templates.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    # only loaded in demonstration mode
    # 'demo': [
    #     'demo/demo.xml',
    # ],
}

