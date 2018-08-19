import django
from flask import jsonify, request
from flask_restful import Resource
from userservice.db.user_models.models import UserData as users
from userservice.utility.user_utilities import get_user_dict

django.setup()


class Users(Resource):
    def get(self, username=None):
        if username:
            user = users.objects.get(username=username)
            user_dict = get_user_dict(user)
            return jsonify({"user": user_dict})
        all_user = users.objects.all()
        user_list = [get_user_dict(entry) for entry in all_user]
        return jsonify({"users": user_list})

    def post(self):
        data = request.get_json(force=True)
        user = users(username=data['username'],
                     password=data['password'],
                     first_name=data['first_name'],
                     middle_name=data['middle_name'],
                     last_name=data['last_name'],
                     phone=data['phone'],
                     email=data['email'],
                     gender=data["gender"],
                     city=data['city'])
        user.save()
        user_dict = get_user_dict(user)
        return jsonify({"User": user_dict})

    def put(self, username=None):
        data = request.get_json()
        if username:
            update = users.objects.get(username=username)
            update.city = data['newCity']
            update.phone = data['newPhone']
            user_dict = get_user_dict(update)

            return jsonify({"Update": user_dict})
        else:
            return jsonify({"Message": "Not updated"})

    def delete(self, username=None):
        data = request.get_json()
        if username:
            delete = users.objects.filter(username=username).delete()
            return jsonify({"Delete": username})
        else:
            return jsonify({"Message": "Invalid Username"})

