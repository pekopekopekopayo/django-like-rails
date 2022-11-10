
from lib.errors.unauthorized import Unauthorized


def authentication(result):
    if not result:
        raise Unauthorized
