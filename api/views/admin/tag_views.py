from django.shortcuts import get_object_or_404
from rest_framework.views import APIView, Response

from api.models.tag.models import Tag
from api.policy.admin.admin_policy import AdminPolicy
from api.serializer.admin.tag_serializer import TagSerializer
from lib.policy.policy import authentication

class TagView(APIView):

    def get(self, req):
        authentication(AdminPolicy(req.current_user).get())

        tags = Tag.objects.all()

        return Response(TagSerializer(tags, many=True).data, status=200)

    def post(self, req):
        authentication(AdminPolicy(req.current_user).post())

        tag = TagSerializer(data=req.data)

        tag.is_valid(raise_exception=True)
        tag.save()

        return Response(tag.data, status=201)

    def put(self, req, name):
        tag = get_object_or_404(Tag, name=name)

        authentication(AdminPolicy(req.current_user, tag).put())

        tag = TagSerializer(instance=tag, data=req.data)

        tag.is_valid(raise_exception=True)
        tag.save()

        return Response(tag.data, status=200)

    def delete(self, req, name):
        tag = get_object_or_404(Tag, name=name)

        authentication(AdminPolicy(req.current_user, tag).delete())

        tag.delete()

        return Response({}, status=204)
