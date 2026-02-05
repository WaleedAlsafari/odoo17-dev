from odoo import models, fields, api
from odoo.exceptions import ValidationError


class libraryBook(models.Model):
    _name = 'library.book'

    name = fields.Char()
    author = fields.Char()
    isbn = fields.Char()
    pages = fields.Integer()
    price = fields.Float()
    total_price = fields.Float(    
    compute="_compute_total_price",
    store=True
    )
    available = fields.Boolean()
    state = fields.Selection([
        ('available','Available'),
        ('borrowed','Borrowed'),
        ('draft','Draft')
    ], 
    default='draft')
    description = fields.Text()
    

    @api.constrains('pages')
    def check_pages(self):
        for rec in self:
            if rec.pages <=0:
                raise ValidationError('Pages must be greater than 0')
            
    @api.constrains('price')
    def check_price(self):
        for rec in self:
            if rec.price <=0:
                raise ValidationError('price must be greater than 0')
    _sql_constraints = [
        ('unique_isbn','unique(isbn)','This isbn is already in use, please try again!',),
        ('check_price','check(price >0)','Plase enter a valid price')
    ]

    def _action_set_available(self):
        for rec in self:
            rec.state = 'available'

    def _action_set_borrowed(self):
        for rec in self:
            rec.state = 'borrowed'

    @api.depends('price')
    def _compute_total_price(self):
        for rec in self:
            rec.total_price = rec.price * 1.15




    