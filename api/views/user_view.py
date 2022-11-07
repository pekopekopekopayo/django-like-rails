from rest_framework.views import APIView
from rest_framework.response import Response
from api.serializer.user_serializer import UserSerializer
from lib.errors.password_not_valid import PasswordNotValid

class UserView(APIView):
    
    def post(self, req):
        if req.data["password"] != req.data["check_password"]:
            raise PasswordNotValid
        user = UserSerializer(data=req.data)

        user.is_valid(raise_exception=True)
        user.save()
        
        return Response(user.data)

        