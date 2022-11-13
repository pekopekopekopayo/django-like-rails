from rest_framework import serializers

from api.models.tag.models import Tag

class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = ('name')
