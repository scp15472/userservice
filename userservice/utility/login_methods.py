from userservice.utility.user_methods import get_user_dict


def get_login_dict(login_object):
    return{"user":get_user_dict(login_object.user),
           "login_time":login_object.login_time,
           "token":login_object.token,
           "logout_time":login_object.logout_time,
           "is_active":login_object.is_active,
           "device_id":login_object.device_id
           }
