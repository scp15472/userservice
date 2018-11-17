from datetime import datetime


def update_login(login_object,data):
    if 'is_active' in data:
        login_object.is_active = False
        login_object.logout_time = datetime.now()
    login_object.save()
    return login_object

