import pdb
from django.shortcuts import get_object_or_404
from rest_framework import serializers
from api.models.book.models import Book
from api.models.user.models import User
from api.serializer.user_serializer import UserSerializer
from rest_framework.exceptions import ValidationError

class BookSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    user_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Book
        fields = ('user', 'user_id', 'id', 'name', 'discribe','price', 'quantity')

    def validate_price(self, price):
        if price <= 0: raise ValidationError('가격은 0보다 커야합니다.')
        return price

    def validate_quantity(self, quantity):
        if quantity <= 0: raise ValidationError('수량은 0보다 커야합니다.')
        return quantity

    def create(self, data):
        data['user'] = User.objects.get(id=data['user_id'])
        return Book.objects.create(**data)


    def update(self, instance, data):
        data['user'] = User.objects.get(id=data['user_id'])

        instance.user = data.get('user', instance.user)
        instance.name = data.get('name', instance.name)
        instance.discribe = data.get('discribe', instance.discribe)
        instance.price = data.get('price', instance.price)
        instance.quantity = data.get('quantity', instance.quantity)

        instance.save()

        return instance
