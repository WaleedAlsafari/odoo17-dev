from urllib.parse import parse_qs

from odoo import http
from odoo.http import request
import json


def valid_response(data,code):
    response = {
        "data" : data
    }

    return request.make_json_response(
                    response,
                    status=code
                ) 
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
    def get_property(self, property_id=None ):

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

    @http.route(route="/api/delete/property/<int:property_id>", methods=["DELETE"], type="http", auth="none", csrf=False)
    def delete_property(self, property_id):
        if not property_id:
            return request.make_json_response(
                    {
                        "message" : "Please enter a valid id"
                    }, status=400
                )
        try:
            res = request.env['estate.property'].sudo().search([('id','=',property_id)])
            if not res:
                return request.make_json_response(
                    {
                        "message" : "property doesn't exist"
                    }, status=404
                )

            print(res.name)
            res.unlink()

            if res:
                return request.make_json_response(
                    {
                        "message" : "property deleted successfully"
                    }, status=200
                )
        except Exception as error:
            return request.make_json_response(
                    {
                        "message" : error
                    }, status=400
                )

    @http.route('/api/get/properties', methods=['GET'], type='http', auth='none', csrf=False)
    def get_property(self):
        try:
            res = request.env['estate.property'].sudo().search([])

            if not res:
                return request.make_json_response({'error': 'No property found'}, status=404)
            
            
            return valid_response(
                [{"id" : rec.id,
                "name" : rec.name
                } for rec in res],
                status=200
            )  
        except Exception as error:
            return request.make_json_response(
                    {
                        "message" : error
                    }, status=400
                )

    @http.route('/api/get/filter/properties', methods=['GET'], type='http', auth='none', csrf=False)
    def get_property(self,state):
        try:
            params = parse_qs(request.httprequest.query_string.decode('utf-8'))
            property_domain = []
            if params.get('state'):
                property_domain = [('state','=',params.get('state')[0])]    

            res = request.env['estate.property'].sudo().search(property_domain)

            if not res:
                return request.make_json_response({'error': 'No property found'}, status=404)
            
            
            return valid_response(
                [{"id" : rec.id,
                "name" : rec.name
                } for rec in res],
                code=200
            )  
        except Exception as error:
            return request.make_json_response(
                    {
                        "message" : error
                    }, status=400
                )