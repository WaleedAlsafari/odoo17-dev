{
    'name': "Real Estate",
    'version': '1.0',
    'depends': ['base'],
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
    ],
    'application': True

  
}