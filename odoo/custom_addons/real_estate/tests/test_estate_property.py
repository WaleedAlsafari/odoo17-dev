from odoo.tests.common import TransactionCase
from odoo import fields

class TestEstateProperty(TransactionCase):


    def setUp(self, *args, **kwargs):
        super(TestEstateProperty, self).setUp()

        self.property_01_record = self.env['estate.property'].create({
            'ref' : 'PRT00005',
            'name' : 'property5',
            'postcode' : '12345',
            'bedrooms' : 5

        })


    def test_01_property_values(self):
        property_id = self.property_01_record

        self.assertRecordValues(property_id,[{
            'ref' : 'PRT00005',
            'name' : 'property5',
            'postcode' : '12345',
            'bedrooms' : 5

        }])