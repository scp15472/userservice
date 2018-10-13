from userservice.db.user_models.models import UserData


def get_single_user(username):
    try:
        user_objects = UserData.objects.get(username=username)
        return user_objects
    except Exception as e:
        print e
        return None


def get_all_user():
    return UserData.objects.all()
