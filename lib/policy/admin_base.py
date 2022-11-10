def is_admin(user):
    return user.id and user.role == 0
