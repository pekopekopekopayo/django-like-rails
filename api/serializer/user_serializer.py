import pdb
from rest_framework import serializers
from api.models.user.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('name', 'email', 'password', 'role')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, data):
        user = User(**data)
        user.to_hash_password()
        user.save()
        return user
