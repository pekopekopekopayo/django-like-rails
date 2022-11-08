from rest_framework.exceptions import APIException

class NotFound(APIException):
    status_code = 404
    default_detail = "레코드가 존재하지 않습니다."
