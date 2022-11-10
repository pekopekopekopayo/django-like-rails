import pdb
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView, Response
from api.models.book.models import Book

from api.policy.admin.book_policy import BookPolicy
from api.serializer.admin.book_serializer import BookSerializer
from lib.policy.policy import authentication

class AdminBookView(APIView):

    def get(self, req):
        authentication(BookPolicy(req.current_user).get())

        books = Book.objects.filter(user_id=req.current_user.id)
        return Response(BookSerializer(books, many=True).data, status=200)

    def post(self, req):
        authentication(BookPolicy(req.current_user).post())

        req_data = req.data
        req_data['user_id'] = req_data.get('user_id') or req.current_user.id

        book = BookSerializer(data=req_data)

        book.is_valid(raise_exception=True)
        book.save()

        return Response(book.data, status=201)

    def put(self, req, id):
        book = Book.objects.get(id=id, user=req.current_user)

        authentication(BookPolicy(req.current_user, book).put())

        req_data = req.data
        req_data['user_id'] = req_data.get('user_id') or req.current_user.id

        book = BookSerializer(instance=book, data=req_data)
        book.is_valid(raise_exception=True)
        book.save()

        return Response(book.data, status=200)

    def delete(self, req, id):
        book = get_object_or_404(Book, id=id, user=req.current_user)
        authentication(BookPolicy(req.current_user, book).delete())

        book.delete()

        return Response({}, status=204)
