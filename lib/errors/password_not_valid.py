from rest_framework.exceptions import APIException

class PasswordNotValid(APIException):
    status_code = 422
    default_detail = "패스워드가 일치하지 않습니다."
