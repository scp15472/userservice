from userservice.db.user_models.models import UserData


def delete_user(username):
    user_objects = UserData.objects.filter(username=username).delete
    return  user_objects
