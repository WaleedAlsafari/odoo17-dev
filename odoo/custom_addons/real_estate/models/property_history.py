from odoo import models, fields


class PropertyHistory(models.Model):
    _name='property.history'
    _description = 'Property History'
    _inherit = ['mail.thread','mail.activity.mixin']

    user_id = fields.Many2one('res.users')
    property_id = fields.Many2one('estate.property')
    old_state = fields.Char()
    new_state = fields.Char()
    reason = fields.Char()
    line_ids = fields.One2many('property.history.line','property_history_id')




class PropertyHistoryLine(models.Model):
    _name='property.history.line'

    description = fields.Char()
    area = fields.Float()

    property_history_id = fields.Many2one('property.history')

