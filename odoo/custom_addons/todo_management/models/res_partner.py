from odoo import models, fields



class ResPartner(models.Model):

    _inherit = 'res.partner'

    todo_ids = fields.One2many(
        'todo.task',
         'assign_to_id'
    )
    
   
