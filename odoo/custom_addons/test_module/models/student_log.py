from odoo import fields, models, api, _

class Student(models.Model):
    
    _name = 'penygon.student.log'
    
    student_id = fields.Many2one('penygon.student')
    
    