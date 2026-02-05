from odoo import fields, models, api, _
from datetime import datetime

class School(models.Model):
    
    _name = 'penygon.school'
    
    name = fields.Char(string="Name", required=True)
    average_aggregate =  fields.Float(string="AVG Aggr.")
    date = fields.Date(string="Date of Establishment")
    datetime_t = fields.Datetime(string="Datetime")
    student_ids = fields.One2many('penygon.student', 'school_id', 'Students')
    
    
    @api.model
    def default_get(self, fields):
        #For prefilling or applying the values onto a form by default
        res = super(School, self).default_get(fields) #base functionality calling
        res.update({'date': datetime.now().date(), 'datetime_t': datetime.now()})#custom changes
        return res
    
    
    