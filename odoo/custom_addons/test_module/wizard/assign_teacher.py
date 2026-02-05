from odoo import fields, models, api, _
from datetime import datetime

class AssignTeacher(models.TransientModel):
    
    _name = 'assign.teacher'
    
    name = fields.Char("Old name")
    new_name = fields.Char("Enter New Name")
    
    @api.model
    def default_get(self, fields):
        res = super(AssignTeacher, self).default_get(fields)
        #custom code block
        context = self.env.context
        active_model = context.get('active_model', '')
        active_id = context.get('active_id', '')
        student = self.env[active_model].browse(active_id)
        res.update({'name': student.name})
        return res
    
   
    def set_teacher(self):
        
        context = self.env.context
        active_ids = context.get('active_ids', [])
        for active_id in active_ids:
            active_model = context.get('active_model', '')
            current_user = self.env.user.name
            student = self.env[active_model].browse(active_id)
            new = self.new_name
            student.name = new
        return True