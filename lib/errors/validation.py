from rest_framework.exceptions import APIException

class BadRequest(APIException):
    def __init__(self, default_detail='요청 값이 잘못 되었습니다.'):
        self.status_code = 422
        self.default_detail = default_detail
        self.default_code = 'service_unavailable'