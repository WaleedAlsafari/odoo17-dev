from odoo import models,fields



class saleOrder(models.Model):
    _inherit = 'sale.order'

    property_id = fields.Many2one('estate.property')

    def action_confirm(self):
        rec = super(saleOrder,self).action_confirm()
        print('Within the confirm button')
        return rec
    

    
    