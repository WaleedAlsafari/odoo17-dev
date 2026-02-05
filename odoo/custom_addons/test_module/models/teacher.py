from odoo import fields, models, api, _

class Teacher(models.Model):
    
    _name = 'penygon.teacher'
    
    name = fields.Char(string="Name", required=True)
    user_id =  fields.Many2one('res.users', 'Related User')
    student_ids = fields.Many2many('penygon.student', 'teacher_student_rel', 'teacher_id', 'student_id', 'Students')