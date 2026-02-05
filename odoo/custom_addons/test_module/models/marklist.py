from odoo import fields, models, api, _

class Marklist(models.Model):
    
    _name = 'penygon.marklist'
    
    @api.model
    def default_get(self, fields):
        res = super(Marklist, self).default_get(fields)
        user = self.env.user
        teacher =  self.env['penygon.teacher'].search([('user_id', '=', user.id)], limit=1)
        if teacher:
            res.update({'teacher_id':  teacher.id})
        return res
    
    name = fields.Char(string="Name", required=True)
    student_id = fields.Many2one('penygon.student', 'Student')
    marks = fields.Float("Mark")
    out_of = fields.Float("Out of", default=50)
    teacher_id = fields.Many2one('penygon.teacher', 'Teacher')
    percentage = fields.Float(compute='_get_percentage', string='Percentage')
    student_school_id = fields.Many2one(related='student_id.school_id', string="School")
    status = fields.Selection([('pass', 'Pass'), ('fail', 'Fail')], "Status")
    progress_card = fields.Binary("Attach Progress Card")
    
    
    @api.depends('marks', 'out_of')
   
    def _get_percentage(self):
        for marklist in self:
            marklist.percentage = marklist.marks / marklist.out_of * 100
            
            
        