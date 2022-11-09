import traceback

from django.http import HttpResponse
from config import settings
from lib.token import current_user
import pdb

class UserTokenGate:
    def __init__(self, get_response):
        self.get_response = get_response
        self.skip_list = [
                            '/api/login',
                            '/api/users',
                         ]

    def __call__(self, request):
        if not request.META.get('HTTP_AUTHORIZATION'):
            return self.get_response(request)

        token = request.META.get('HTTP_AUTHORIZATION').split()[-1]

        if request.META['PATH_INFO'] not in self.skip_list:
            try:
                request.current_user = current_user(token)
            except:
                return HttpResponse("유효하지 않은 토큰입니다.", status=401)

        return self.get_response(request)
