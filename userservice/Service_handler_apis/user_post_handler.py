from userservice.db.user_models.models import UserData


def create_user(data):
    try:
        username = data['username']
        password = data['password']
        first_name = data['first_name']
        middle_name = data['middle_name']
        last_name = data['last_name']
        gender = data['gender']
        phone = data['phone']
        city = data['city']
        email = data['email']
    except Exception as e:
        print e
        raise e
    user_objects=UserData.objects.create(username=username,
                                      password=password,
                                      first_name=first_name,
                                      middle_name=middle_name,
                                      last_name=last_name,
                                      gender=gender,
                                      phone=phone,
                                      city=city,
                                      email=email)
    return user_objects


