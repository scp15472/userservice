from flask import Flask
from flask_restful import Api
import django

from userservice.service_apis.login1 import Login1
from userservice.service_apis.user1 import User1

django.setup()

app = Flask(__name__)

api = Api(app, prefix='/userservice/')

api.add_resource(User1, 'user', 'user/<username>')
api.add_resource(Login1, 'login', 'login/<token>')


if __name__ == "__main__":
    app.run(host='localhost', port=2005, debug=True)
