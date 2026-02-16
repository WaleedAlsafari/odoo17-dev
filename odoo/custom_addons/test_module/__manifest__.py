# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'Training module',
    'version' : '0.1',
    'summary': 'Training purpose',
    'sequence': 15,
    'description': """
    Training and testing 
 """,
    'category': 'Training',
    # 'website': 'https://www.odoo.com/page/billing',
    # 'images' : ['images/accounts.jpeg','images/bank_statement.jpeg','images/cash_register.jpeg','images/chart_of_accounts.jpeg','images/customer_invoice.jpeg','images/journal_entries.jpeg'],
    'depends' : ['base'],
    'data': [
        'security/training_security.xml',
        'security/ir.model.access.csv',
        'wizard/assign_teacher_view.xml',
        'views/school_view.xml',
        'views/student_view.xml',
        'views/teacher_view.xml',
        'views/marklist_view.xml',
        'views/menu.xml',
        
    ],
    
    'installable': True,
    'auto_install': False,
}
