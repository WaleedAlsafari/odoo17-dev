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
        'security/ir.model.access.csv',
        'views/base_menu.xml',
        'views/property_view.xml',
        'views/owner_view.xml',
        'views/tag_view.xml',
        'views/sale_order_view.xml',
        'views/building_view.xml',
        'reports/property_report.xml',
        
    ],
    
    'assets' : { 
        'web.assets_backend' : ['real_estate/static/src/css/property.css']
    },
    'application': True

  
}