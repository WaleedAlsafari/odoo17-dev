from odoo import fields, models, api, _

class Student(models.Model):
    
    _name = 'penygon.student'
    
    name = fields.Char(string="Name", required=True)
    school_id = fields.Many2one('penygon.school', string="School")
    teacher_ids = fields.Many2many('penygon.teacher', 'teacher_student_rel', 'student_id', 'teacher_id', 'Teachers')
    active = fields.Boolean(string="Active", default=True)
    image = fields.Binary("Photo")
    student_log_ids = fields.One2many('penygon.student.log', 'student_id', 'Logs')
    
    @api.model
    def default_get(self, fields):
        #For prefilling or applying the values onto a form by default
        res = super(Student, self).default_get(fields) #base functionality calling
        school = self.env['penygon.school'].search([('name', 'ilike', 'VMSC School')])
        school_ids = school.ids
        schools = self.env['penygon.school'].browse(school_ids)
        res.update({'school_id': school_ids[1]})#custom changes
        return res
    

    @api.returns('self', lambda value: value.id)
    def copy(self, default=None):
        default = dict(default or {})
        if 'student_log_ids' not in default:
            default.update({'student_log_ids': []})
        return super(Student, self).copy(default=default)
    
    @api.model
    def create(self, values):
        res = super(Student, self).create(values) #base functionality calling
        self.env['penygon.student.log'].create({'student_id': res.id}) #custom changes
        return res
        
    

    def write(self, values):
        res = super(Student, self).write(values) 
        return res
    

    def action_set_deactive(self):
        for student in self:
            student.active = False
    

    def action_set_active(self):
        for student in self:
            student.active = True
        
        