from odoo import api, models, fields
from odoo.exceptions import ValidationError



class TodoTask(models.Model):
    _name='todo.task'
    _inherit = ['mail.thread','mail.activity.mixin']
    active = fields.Boolean(default=True)

    ref = fields.Char(default ='New', readonly=1)
    name = fields.Char(required=1)
    description = fields.Text()
    assign_to_id = fields.Many2one('res.users', required=1)
    due_date = fields.Date(required=1)
    estimated_time = fields.Float(
        digits=(4, 1),
        required=1
    )
    total_duration = fields.Float(
        digit=(4,1),
        compute='_sum_duration'
    )
    is_late = fields.Boolean(default=False)
    status = fields.Selection(
        [
            ('new','New'),
            ('in progress', 'In Progress'),
            ('completed','Completed'),
            ('closed','Closed')
        ],
        tracking='1'
    )
    is_managers_group = fields.Boolean(compute="_check_if_manager_group")

    line_ids = fields.One2many(
        'todo.line',
        'todo_id'

    )

    @api.model_create_multi
    def create(self,vals):
        rec = super(TodoTask,self).create(vals)
        print("Create function have been called")
        rec.status='new'
        rec._check_estimated_time_exceeded()
        return rec
    
    def write(self,vals):
        rec = super(TodoTask,self).write(vals)
        for rec in self:
            if rec.status == 'closed' and 'status' not in vals:
                raise ValidationError("You can't update a closed task")
            rec._check_estimated_time_exceeded()
        return rec        


    def action_mark_in_progress(self):
        for rec in self:
            if not rec.env.user.has_group('todo_management.todo_managers_group'):
                raise ValidationError("You are not allowed to do this action")
            rec.status='in progress'
            rec.ref= self.env['ir.sequence'].next_by_code('todo_seq')

    def action_mark_completed(self):
        self.status='completed'

    def action_mark_closed(self):
        for rec in self:
            if not rec.env.user.has_group('todo_management.todo_managers_group'):
                raise ValidationError("You are not allowed to do this action")
            rec.status='closed'
        
    @api.depends('line_ids.duration')
    def _sum_duration(self):
        for rec in self:
            rec.total_duration = sum(rec.line_ids.mapped('duration'))

    def _check_estimated_time_exceeded(self):
        for rec in self:
            if rec.total_duration > rec.estimated_time:
                raise ValidationError('Total duration must not exceed estimated time')
    
    def _check_if_late(self):
        self = self.search([])
        for rec in self:
            if rec.due_date < fields.Date.today() and rec.status in ('new','in progress'):
                rec.is_late = True
                print(rec.is_late)
    
    def action(self):
        print(self.assign_to_id)
        print(self.search(['|',('estimated_time','=','20.0'),('name','=','Task 3')]))


    def open_assign_bulk_partner_wizard(self):
        action = self.env.ref('todo_management.assign_bulk_partner_action').read()[0]
        action['context'] = {
        'default_todo_ids': self.ids,
    }
        return action
    
    def _check_if_manager_group(self):
        for rec in self:
            if not rec.env.user.has_group('todo_management.todo_managers_group'):
                rec.is_managers_group=False
            else:
                rec.is_managers_group=True
        



    
    
class TodoLine(models.Model):
    _name='todo.line'

    todo_id = fields.Many2one(
        'todo.task'
    )
    
    note = fields.Text(requried=1)
    date = fields.Date(requried=1)
    duration = fields.Float(
        digits=(4, 1),
        required=1,
        string='Duration (Hours)'
    )

    
    
    
  
    


