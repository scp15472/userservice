from userservice.db.user_models.models import UserData, Login


def create_login(data):
    try:
        user = data['username']
        password = data['password']
        device_id = data['device_id']
    except Exception as e:
        print e
        raise e
    try:
        user_objects = UserData.objects.get(username=user, password=password)
    except Exception as e:
        print e
        raise e
    login_objects= Login.objects.create(user=user_objects,
                                        device_id=device_id)
    return login_objects