from odoo import models, fields
from odoo.exceptions import ValidationError


class AssignBulkPartner(models.TransientModel):
    _name = 'assign.bulk.partner'

    todo_ids = fields.Many2many('todo.task', string='Selected Tasks')
    assign_to_id = fields.Many2one('res.partner', required=1)



    def confirm_action(self):
        for task in self.todo_ids:
            if task.status == 'closed':
                raise ValidationError("You can't edit closed tasks")
        self.todo_ids.write({
            'assign_to_id' : self.assign_to_id
        })