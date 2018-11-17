import django;
from flask import jsonify, request, make_response, json, Response
from flask_restful import Resource

from userservice.Service_handler_apis import login_post_handler, \
    login_get_handler, login_put_handler, login_delete_handler
from userservice.utility import login_methods

django.setup()


class Login1(Resource):
    def post(self):
        data = request.get_json()
        login_objects = login_post_handler.create_login(data)
        response_dict = login_methods.get_login_dict(login_objects)
        response = make_response(json.dumps({"Login": response_dict}))
        response.mimetype = 'application/json'
        response.set_cookie('token', login_objects.token)
        return response

    def get(self, token=None):
        if not token:
            token = request.cookies.get('token')
            login_objects = login_get_handler.get_single_login(token)
            if login_objects:
                response_dict = login_methods.get_login_dict(login_objects)
                return jsonify({"Login": response_dict})


        # filters = request.args
        # login_objects = login_get_handler.get_login_by_filter(filters)
        # response_dict = [login_methods.get_login_dict(login) for login in login_objects]
        # return jsonify({"Login": response_dict})

    def put(self, token):
        login_objects = login_get_handler.get_single_login(token)
        if login_objects:
            data = request.get_json()
            login_objects = login_put_handler.update_login(login_objects, data)
            response_dict = login_methods.get_login_dict(login_objects)

            response = make_response(json.dumps({"Login": response_dict}))
            response.mimetype = 'application/json'
            response.set_cookie("token", None)
            return response

            return jsonify({"Login": response_dict})
        else:
            return jsonify({"Message": "User Login not found!!!"})

    def delete(self, token):
        login_objects = login_get_handler.get_single_login(token)
        if login_objects:
            login_objects = login_delete_handler.delete_login(token)
            return jsonify({"Login": "LogOut successfully"})
        else:
            return jsonify({"Message": "Login is not deleted"})
