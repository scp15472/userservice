import django;
from flask import jsonify, request
from flask_restful import Resource

from userservice.Service_handler_apis import user_post_handler, \
    user_get_handler, user_put_handler, user_delete_handler
from userservice.utility import user_methods

django.setup()


class User1(Resource):
    def post(self):
        data = request.get_json()
        user_objects = user_post_handler.create_user(data)
        response_dict = user_methods.get_user_dict(user_objects)
        return jsonify({"User": response_dict})

    def get(self, username=None):
        if username:
            user_objects = user_get_handler.get_single_user(username)
            response_dict = user_methods.get_user_dict(user_objects)
            return jsonify({"User": response_dict})
        else:
            user_objects = user_get_handler.get_all_user()
            response_dict = [user_methods.get_user_dict(user_object) for
                             user_object in user_objects]
            return jsonify({"user": response_dict})

    def put(self,username):
        user_objects = user_get_handler.get_single_user(username)
        if user_objects:
            data = request.get_json()
            user_objects = user_put_handler.update_user(user_objects,data)
            response_dict = user_methods.get_user_dict(user_objects)
            return jsonify({"User":response_dict})
        else:
            return jsonify({"Message": "User not found!!!"})

    def delete(self,username):
        user_objects = user_get_handler.get_single_user(username)
        if user_objects:
            user_objects = user_delete_handler.delete_user(username)
            return jsonify({"User": "User is Deleted"})
        else:
            return jsonify({"Message":"User is not deleted"})