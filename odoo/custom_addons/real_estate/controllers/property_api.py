from odoo import http
from odoo.http import request
import json
class PropertyApi(http.Controller):
    
    @http.route(route='/api/create/property', methods=['POST'], type='http', auth='none', csrf=False)
    def post_property(self):
        args = request.httprequest.data.decode()
        vals = json.loads(args)
        if not vals.get('name'):
            return request.make_json_response(
                    {
                        "error" : 'property name is messing'
                    }, status=400
                ) 
        try:
            res = request.env['estate.property'].sudo().create(vals)
            print(res)
            if res:
                return request.make_json_response(
                    {
                        "message" : "Property created successfully",
                        "id" : res.id,
                        "name" : res.name
                    }, status=201
                ) 
        except Exception as error:
            return request.make_json_response(
                    {
                        "message" : error
                    }, status=400
                ) 

    @http.route(route='/api/create/property/json', methods=['POST'], type='json', auth='none', csrf=False)
    def post_property_json(self):
        args = request.httprequest.data.decode()
        vals = json.loads(args)
        res = request.env['estate.property'].sudo().create(vals)
        if res:
            return {
                "message" : "Property created successfully"
            }

    @http.route('/api/get/property', methods=['GET'], type='http', auth='none', csrf=False)
    def get_property(self, property_id=None, ):

        if not property_id:
            return request.make_json_response({'error': 'id is required'}, status=400)

        res = request.env['estate.property'].sudo().search(
            [('id', '=', property_id)],
         
        )

        if not res:
            return request.make_json_response({'error': 'Not found'}, status=404)

        return request.make_json_response(
            {"name": res.name},
            status=200
        )  

    @http.route(route='/api/update/property/<int:property_id>', methods=['PUT'], type='http', auth='none', csrf=False)
    def update_property(self, property_id):
        if not property_id:
            return request.make_json_response(
            {
                "error" : "Please enter a valid id"
            }, status=400
        )
        try:
            res = request.env['estate.property'].sudo().search([('id','=', property_id)])
            args = request.httprequest.data.decode()
            vals = json.loads(args)
            res.write(vals)
            if res:
                return request.make_json_response(
                    {
                        "id" : res.id,
                        "bedrooms" : res.bedrooms
                    }, status=200
                )
        except Exception as error:
            return request.make_json_response(
                    {
                        "message" : error
                    }, status=400
                )