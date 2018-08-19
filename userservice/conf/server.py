from flask import Flask
from flask_restful import Api
import django

from userservice.service_apis.login import Logins
from userservice.service_apis.user import Users

django.setup()

app = Flask(__name__)

api = Api(app, prefix='/users/')

api.add_resource(Users, 'user', 'user/<username>')
api.add_resource(Logins, 'login', 'login/<token>')


if __name__ == "__main__":
    app.run(host='localhost', port=2005, debug=True)
