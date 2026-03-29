from odoo import http
from odoo.http import request
import json


class TodoApi(http.Controller):


    @http.route(route='/api/task/post', methods=["POST"], type='http', auth='none', csrf=False)
    def post_task(self):
        args = request.httprequest.data.decode()
        vals = json.loads(args)

        if not vals.get('name'):
            return request.make_json_response(
                {
                    'error': 'name is requried!'
                }, status=400
            )
        
        try:
            res = request.env['todo.task'].sudo().create(vals)

            if res:
                return request.make_json_response(
                    {
                        'message' : 'task created successfully',
                        'name' : res[0]
                    }, status=201
                )
            
        except Exception as error:
            return request.make_json_response(
                {
                    'message' : error 
                }, status= 400
            )

    @http.route(route='/api/task/get', methods=["GET"], type='http', auth='none', csrf=False)
    def get_task(self, task_id=None):
        
        if not task_id:
            return request.make_json_response(
                {
                    "error": "id is requried"
                }, status=400
            )
        
        res = request.env['todo.task'].sudo().search([("id","=",task_id)])

        if not res:
            return request.make_json_response(
            {
                "error" : "Task not exist"
            }, status=404
            )
        
        return request.make_json_response(
        {
            "name" : res.name
        }, status=201
        )

    @http.route(route='/api/task/update/<int:task_id>', methods=["PUT"], type='http', auth='none', csrf=False)
    def update_task(self, task_id=None):
        
        if not task_id:
            return request.make_json_response(
                {
                    "error": "id is requried"
                }, status=400
            )

        try:
            res = request.env['todo.task'].sudo().search([("id","=",task_id)])
            args = request.httprequest.data.decode()
            vals = json.loads(args)
            res.write(vals)

            if res:
                return request.make_json_response(
                    {
                        "message" : "task updated successfully",
                        "estimated_time" : res.estimated_time
                    }, status=201
                )
        except Exception as error:
            return request.make_json_response(
                {
                    "message" : error
                }, status=400
            )


    @http.route(route="/api/task/delete", methods=["DELETE"], type="http", auth="none", csrf=False)
    def unlink_task(self, task_id=None):
        
        if not task_id:
            return request.make_json_response(
                {
                    "message" : "id is requried!"
                }, status=400
            )

        try:
            res = request.env["todo.task"].sudo().search([("id","=",task_id)])
            res.unlink()

            if res:
                return request.make_json_response({
                    "message" : "task deleted successfully"
                    
                }, status=201)
        except Exception as error:
            return request.make_json_response({
                "message" : error
            }, status=400)
        

    