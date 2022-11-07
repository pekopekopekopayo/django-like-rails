import pdb
from rest_framework.exceptions import APIException

class BadRequest(APIException):
    status_code = 422
    default_code = 'service_unavailable'
    default_detail = '요청값이 잘못 되었습니다.'

class UnprocessableEntity(APIException):
    status_code = 422
    default_code = 'service_unavailable'