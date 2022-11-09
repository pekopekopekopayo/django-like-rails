import datetime as dt
import jwt
import os
from api.models.user.models import User
from config.settings import ALGORITHM, SECRET_KEY

def set_token(email):
    payload = {
                "email": email,
                "expires": dt.datetime.now().timestamp()
            }
    return jwt.encode(payload, SECRET_KEY, ALGORITHM)


def get_token(token):
    payload = jwt.decode(token, SECRET_KEY, ALGORITHM)
    expires = int(payload.get('expires'))

    if dt.datetime.now().timestamp() >= expires + (60 * os.environ.get('EXPIRES_TIME')):
        return False
    elif dt.datetime.now().timestamp() >= expires + (60 * 60 * 24 * os.environ.get('REFRASH_EXPIRES_TIME')):
        return set_token(payload['email'])
    return payload

def current_user(token):
    user_info = jwt.decode(token, SECRET_KEY, ALGORITHM)
    user = User.objects.filter(email=user_info['email']).first()
    return user
