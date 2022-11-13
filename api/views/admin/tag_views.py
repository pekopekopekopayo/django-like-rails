from django.shortcuts import get_object_or_404
from rest_framework.views import APIView, Response

from api.models.tag.models import Tag
from api.serializer.admin.tag_serializer import TagSerializer

class BookView(APIView):

    def get(self, req):
        tags = Tag.objects.all()

        return Response(TagSerializer(tags, many=True).data, status=200)

    def post(self, req):
        tag = TagSerializer(data=req.datqa)

        tag.is_valid(raise_exception=True)
        tag.save()

        return Response(tag.data, status=201)

    def put(self, req, id):
        tag = get_object_or_404(Tag, id=id)

        tag = TagSerializer(data=req.datqa)

        tag.is_valid(raise_exception=True)
        tag.save()

        return Response(tag.data, status=200)

    def delete(self, req, id):
        tag = get_object_or_404(Tag, id=id)
        tag.delete()

        return Response({}, status=204)
