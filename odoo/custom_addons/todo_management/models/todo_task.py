from odoo import models, fields



class TodoTask(models.Model):
    _name='todo.task'
    _inherit = ['mail.thread','mail.activity.mixin']

    name = fields.Char(required=1)
    description = fields.Text()
    assign_to_id = fields.Many2one('res.partner')
    due_date = fields.Date()
    status = fields.Selection(
        [
            ('new','New'),
            ('in progress', 'In Progress'),
            ('completed','Completed')
        ],
        tracking='1'
    )

    def action_mark_new(self):
        self.status='new'

    def action_mark_in_progress(self):
        self.status='in progress'

    def action_mark_completed(self):
        self.status='completed'

    
   
