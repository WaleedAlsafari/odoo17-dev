from odoo import models, fields



class Building(models.Model):
    _name='building'
    _inherit = ['mail.thread','mail.activity.mixin']
    _description = 'New Building'
    _rec_name= 'code'

    num = fields.Integer()
    code = fields.Char()
    description = fields.Text()
    active = fields.Boolean(default=True)

 

   


    
   
