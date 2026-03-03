from odoo import models,fields,api
from odoo.exceptions import ValidationError


class estateProperty(models.Model):
    _name = 'estate.property'
    _description = 'Property'
    _inherit = ['mail.thread','mail.activity.mixin']


    ref = fields.Char(default='New', readonly=1)
    name = fields.Char(required=1, size=30, translate=True) 
    description = fields.Text()
    postcode = fields.Char(required=1)
    date_availability = fields.Date(default= fields.Date.today())
    expected_price = fields.Float()
    expected_selling_date = fields.Date()
    is_late = fields.Boolean()
    selling_price = fields.Float(default='200000')  
    diff_price = fields.Float(compute='_compute_diff_price')    
    bedrooms = fields.Integer()
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    garden_orientation = fields.Selection([
        ('north','North'),
        ('east','East'),
        ('south','South'),
        ('west','West'),
    ],default='north')
    # Many to one relation field
    owner_id = fields.Many2one('owner')
    owner_phone = fields.Char(
    string='Ph',
    related='owner_id.phone',
    
    )
    tag_ids = fields.Many2many('tag')
    state= fields.Selection([
        ('draft','Draft'),
        ('pending','Pending'),
        ('sold','Sold'),
        ('closed','closed'),
     
    ],
    default='draft',
    tracking='1'
   )
    line_ids = fields.One2many(
      'property.line',
      'property_id'

    )
    active = fields.Boolean(default=True)

    _sql_constraints = [
        ('unique_name','unique("name")','This name exist, please use different name!')
    ]

    @api.constrains('bedrooms')
    def _check_bedrooms_not_zero(self):
        for rec in self:
            if rec.bedrooms == 0:
                print("not vaild")
                raise ValidationError("Please enter valid bedrooms number!")

    # Below 4 CRUD method are overideed and are optional to write if needs to provide more logic
    @api.model_create_multi
    def create(self,vals):
        rec = super(estateProperty,self).create(vals)
        # if rec.ref == 'New':
        rec.ref= self.env['ir.sequence'].next_by_code('property_seq')
        rec.action_mark_pending()
        print("Create function have been called")
        return rec
    
    @api.model
    def _search(self, domain, offset=0, limit=None, order=None, access_rights_uid=None):
        rec = super(estateProperty,self)._search(domain, offset, limit, order, access_rights_uid)
        print("search method have been called")
        return rec
    
    # Don't use @api because this function deal with record not moduel
    def write(self, vals):
        # for rec in self:
        #     if rec.state == 'sold':
        #         raise ValidationError("You can't edit this property cause it's already sold")
        
        print("write function have been called")
        return super(estateProperty,self).write(vals) 
            
    # Don't use @api because this function deal with record not moduel
    def unlink(self):
        rec = super(estateProperty, self).unlink()
        print("delete function have been called")
        return rec
    
    def _create_history_record(self,old_state,new_state, reason=False):
        for rec in self:
            self.env['property.history'].create(
            {
                'user_id': self.env.uid,
                'property_id': rec.id,
                'old_state': old_state,
                'new_state': new_state,
                'reason' : reason, 
                'line_ids': [(0,0,{'description' : line.description, 'area' : line.area}) for line in rec.line_ids]
            }
       )
        return rec
    
    def action_mark_draft(self):
        self._create_history_record(self.state,'draft')
        for rec in self:
            rec.state='draft'

    def action_mark_pending(self):
        self._create_history_record(self.state,'pending')
        for rec in self:
            rec.state='pending'

    def action_mark_sold(self):
        self._create_history_record(self.state,'sold')
        for rec in self:
            rec.state='sold'
  
    def action_mark_closed(self):
        self._create_history_record(self.state,'closed')
        for rec in self:
            rec.state='closed'

    @api.depends('selling_price','expected_price','owner_id.phone')
    def _compute_diff_price(self):
        for rec in self:
            rec.diff_price = rec.selling_price - rec.expected_price
        print("calculation done")

    @api.onchange('expected_price')
    def _on_negative_expected_price(self):
        for rec in self:
            if rec.expected_price < 0:
                return {
                    'warning' : {'title' : 'warning', 'message' : 'negative vallue', 'type' : 'notification'}
                }
    
    def check_expected_selling_date(self):
        self = self.search([])
        for rec in self:
            if rec.expected_selling_date < fields.Date.today():
                rec.is_late=True
                print(rec.is_late)
            else:
                rec.is_late=False
                print(rec.is_late)

    def show_change_state_wizard(self):
        if self.state =='closed':
            action = self.env['ir.actions.actions']._for_xml_id('real_estate.change_state_wizard_action')
            action['context'] = {'default_property_id' : self.id}
            return action
        else:
            raise ValidationError("You can't change state if it's not closed")
    
    def open_releated_owner_button(self):
        self.ensure_one()
        action = self.env['ir.actions.actions']._for_xml_id('real_estate.owner_action')
        view_id = self.env.ref('real_estate.owner_view_form').id
        action['res_id'] = self.owner_id.id
        action['views'] = [[view_id, 'form']]
        return action
        
        # Another way to peform it ###########################
    #     self.ensure_one()
    #     return {
    #     'type': 'ir.actions.act_window',
    #     'name': 'Owner',
    #     'res_model': 'owner',
    #     'view_mode': 'form',
    #     'res_id': self.owner_id.id,
    #     'target': 'current',
    #  }


class PropertyLine(models.Model):
    _name = 'property.line'

    description = fields.Char()
    area = fields.Float()

    property_id = fields.Many2one(
        'estate.property'
    )


  

        