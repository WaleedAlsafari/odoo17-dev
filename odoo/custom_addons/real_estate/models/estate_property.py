from odoo import models,fields,api
from odoo.exceptions import ValidationError


class estateProperty(models.Model):
    _name = 'estate.property'
    _description = 'Property'
    _inherit = ['mail.thread','mail.activity.mixin']

    name = fields.Char(required=1, default='New', size=10) 
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
        ('completed','Completed'),
     
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
        rec.state='pending'
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
    
    def action_mark_draft(self):
        for rec in self:
            rec.state='draft'

    def action_mark_pending(self):
        for rec in self:
            rec.state='pending'

    def action_mark_sold(self):
        for rec in self:
            rec.state='sold'

    def action_mark_completed(self):
        for rec in self:
            rec.state='completed'

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




class PropertyLine(models.Model):
    _name = 'property.line'

    description = fields.Char()
    area = fields.Float()

    property_id = fields.Many2one(
        'estate.property'
    )

  

        