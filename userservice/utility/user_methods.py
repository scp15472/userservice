def get_user_dict(user_objects):
    return {
            "username": user_objects.username,
            "first_name": user_objects.first_name,
            "middle_name": user_objects.middle_name,
            "last_name": user_objects.last_name,
            "phone": user_objects.phone,
            "email": user_objects.email,
            "gender": user_objects.gender,
            "city": user_objects.city
             }