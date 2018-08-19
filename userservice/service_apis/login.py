import django
from flask import jsonify, request
from flask_restful import Resource
from userservice.db.user_models.models import Login as logins
from userservice.db.user_models.models import UserData
from userservice.utility.user_utilities import get_login_dict

django.setup()

class Logins(Resource):
    def get(self, token=None):
        if token:
            user_Token=logins.objects.get(token=token)
            login_dict=get_login_dict(user_Token)
            return jsonify({"Login": login_dict})
        else:
            return jsonify({"Message": "Invalid Token"})


    def post(self):
        data = request.get_json(force=True)
        try:
            user_obj = UserData.objects.get(username=data['username'],
                                            password=data['password'])

            login = logins(user=user_obj, device_id=data['deviceId'])
            login.save()
            login_dict = get_login_dict(login)
            return jsonify({"Login": login_dict})
        except Exception as e:
            print e
            return "User not found..."





