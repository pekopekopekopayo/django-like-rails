import pdb
from lib.errors.bad_request import BadRequest
from rest_framework import serializers
from app.models.user import User

class UserSerializer(serializers.Serializer):
    class Meta:
        model = User
        fields = ('name', 'email')
    