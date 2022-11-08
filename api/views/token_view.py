import pdb
from rest_framework.views import APIView, Response
from rest_framework.decorators import api_view
from api.models.user.models import User
from lib.errors.not_found import NotFound
from lib.token import set_token

class TokenView(APIView):

    @api_view(['POST'])
    def login(req):
        user = User.objects.filter(email=req.data.get('email')).first()
        if not user.valid_password(req.data.get('password')):
            raise NotFound
        return Response({"token": set_token(user.email)}, status=200)

