from rest_framework.exceptions import APIException

class Unauthorized(APIException):
    status_code = 401
    default_detail = "이 유저는 권한이 없습니다."
