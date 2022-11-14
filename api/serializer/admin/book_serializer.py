import pdb
from django.shortcuts import get_object_or_404
from rest_framework import serializers
from api.models.book.models import Book
from api.models.tag.models import Tag
from api.models.user.models import User
from api.serializer.admin.tag_serializer import TagSerializer
from api.serializer.user_serializer import UserSerializer
from rest_framework.exceptions import ValidationError

class BookSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    user_id = serializers.IntegerField(write_only=True)

    tag_ids = serializers.ListField(write_only=True, required=False)
    tags = TagSerializer(read_only=True, many=True)
    class Meta:
        model = Book
        fields = ('user', 'user_id', 'id', 'name', 'discribe','price', 'quantity', 'tag_ids','tags')

    def validate_price(self, price):
        if price <= 0: raise ValidationError('가격은 0보다 커야합니다.')
        return price

    def validate_quantity(self, quantity):
        if quantity <= 0: raise ValidationError('수량은 0보다 커야합니다.')
        return quantity

    def create(self, data):
        data['user'] = User.objects.get(id=data['user_id'])

        tag_ids = Tag.objects.filter(id__in=data.pop('tag_ids')) if data.get('tag_ids') else []

        book = Book.objects.create(**data)
        book.tags.add(*tag_ids)

        return book


    def update(self, instance, data):
        data['user'] = User.objects.get(id=data['user_id'])

        instance.user = data.get('user', instance.user)
        instance.name = data.get('name', instance.name)
        instance.discribe = data.get('discribe', instance.discribe)
        instance.price = data.get('price', instance.price)
        instance.quantity = data.get('quantity', instance.quantity)
        tag_ids = Tag.objects.filter(id__in=tag_ids) if data.get('tag_ids') else instance.tags.all()
        instance.save()
        instance.tags.remove()
        instance.tags.add(*tag_ids)


        return instance
