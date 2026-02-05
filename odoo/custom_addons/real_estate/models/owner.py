from odoo import models, fields



class Owner(models.Model):
    _name = 'owner'

    name = fields.Char(requried='1', defalut='new')
    phone = fields.Char(requried='1')
    address = fields.Char()

    property_ids = fields.One2many(
        "estate.property",
        "owner_id"
    )
    tag_ids = fields.Many2many('tag')