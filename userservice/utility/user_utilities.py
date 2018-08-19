def get_user_dict(User):
    return {"username": User.username, "first_name": User.first_name,
            "middle_name": User.middle_name, "last_name": User.last_name,
            "phone": User.phone, "email": User.email,
            "gender": User.gender, "city": User.city}

def get_login_dict(Logins):
    return{"user":get_user_dict(Logins.user), "login":Logins.login_time, "token":Logins.token,
           "logout_time":Logins.logout_time, "is_active":Logins.is_active,
           "device_id":Logins.device_id}
