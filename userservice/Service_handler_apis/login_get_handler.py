from userservice.db.user_models.models import Login


def get_single_login(token):
    try:
        login_objects = Login.objects.filter(token=token, is_active=True)
        if login_objects:
            return login_objects[0]
    except Exception as e:
        print e
        return None

def get_login_by_filter(filters):
    criteria = {}
    if 'user' in filters:
        criteria['user']=filters['user']
    login_objects = Login.objects.filter(**criteria)
    return login_objects
