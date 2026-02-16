from odoo import models, fields


class ChangeState(models.TransientModel):
    _name = 'change.state'

    property_id = fields.Many2one('estate.property')
    new_state = fields.Selection([
        ('draft','Draft'),
        ('pending','Pending')
    ])
    reason = fields.Char()



    def confirm_action(self):
        self.property_id.state = self.new_state
        self.property_id._create_history_record('closed',self.new_state, self.reason)