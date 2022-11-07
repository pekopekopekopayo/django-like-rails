import pdb
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
# from app.serializer.user_serializer import UserSerializer

from app.models.user import User
# Create your views here.

class UserView(APIView):
    
    @api_view(['GET'])
    def index(req):
        return Response({"hello": "world"})
        # user = User.objects.all()
        # return UserSerializer(user)

    # @api_view(['GET'])
    # def show(req):
    #     return Response({'some': 'data'})
        
    # @api_view(['POST'])
    # def create(req):
    #     user = User()
    #     return Response(UserSerializer(user), status=201)