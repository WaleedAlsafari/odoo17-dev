{
    'name': "Real Estate",
    'version': '1.0',
    'depends': [
        'base',
        'sale_management',
        'account',
        'mail'
                ],
    'author': "Waleed A",
    'category': 'Category',
    'description': """
    This is a real estate moduel
    """,
    # data files always loaded at installation
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'data/property_seq.xml',
        'views/base_menu.xml',
        'views/property_view.xml',
        'views/property_history_view.xml',
        'views/owner_view.xml',
        'views/tag_view.xml',
        'views/sale_order_view.xml',
        'views/building_view.xml',
        'views/account_move_view.xml',
        'wizard/change_state_wizard.xml',
        'reports/property_report.xml',
    ],
    
    'assets' : { 
        'web.assets_backend' : ['real_estate/static/src/css/property.css'],
        'web.report_assets_common' : ['real_estate/static/src/css/property.css']
    },
    'application': True
    
  
}