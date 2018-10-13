from userservice.db.user_models.models import Login


def delete_login(token):
    login_objects = Login.objects.filter(token=token).delete()
    return login_objects
