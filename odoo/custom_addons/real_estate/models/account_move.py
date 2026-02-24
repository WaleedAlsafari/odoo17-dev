from odoo import models

class AccountMove(models.Model):
    _inherit='account.move'



    def make_somthing_within_account_move(self):
        print(self, 'Within make_somthing_within_account_move')