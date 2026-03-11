{
    'name': "To-Do App",
    'version': '1.0',
    'depends': [
        'base',
        'mail'
                ],
    'author': "Waleed A",
    'category': 'Category',
    'description': """
    This is a To-Do App
    """,
    # data files always loaded at installation
    'data': [
        'security/ir.model.access.csv',
        'data/todo_sequence.xml',
        'views/todo_menu.xml',
        'views/todo_view.xml',
        'views/res_partner_view.xml',
        'wizard/assign_bulk_partner_wizard.xml',
        'reports/todo_report.xml'
        
       
        
    ],
    
    'application': True

  
}