def update_user(user_objects,data):
    if 'city' in data:
        user_objects.city = data['city']
    if 'phone' in data:
        user_objects.phone = data['phone']
    if 'email' in data:
        user_objects.email = data['email']
    user_objects.save()
    return user_objects

