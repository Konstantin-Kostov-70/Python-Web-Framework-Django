from django.core.exceptions import ObjectDoesNotExist
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from DjangoRESTDemo.demo_api.models import Book
from DjangoRESTDemo.demo_api.serializers import BookSerializer


class BookListCreateView(APIView):
    def get(self, request):
        books = Book.objects.all()
        book_get_serializer = BookSerializer(books, many=True)
        return Response(book_get_serializer.data)

    def post(self, request):
        book_post_serializer = BookSerializer(data=request.data)
        if book_post_serializer.is_valid():
            book_post_serializer.save()
            return Response(
                book_post_serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            book_post_serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


class BookGetPutDelete(APIView):
    def get(self, request, pk):
        try:
            book = Book.objects.get(pk=pk)
            book_get_serializer = BookSerializer(book)
            return Response(book_get_serializer.data, status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
            return Response(
                {'message': 'have not found book with this id'},
                status=status.HTTP_404_NOT_FOUND
            )

    def put(self, request, pk):
        try:
            book = Book.objects.get(pk=pk)
            book_put_serializer = BookSerializer(book, data=request.data)
            if book_put_serializer.is_valid():
                book_put_serializer.save()
                return Response(book_put_serializer.data, status=status.HTTP_200_OK)
            return Response(
                book_put_serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

        except ObjectDoesNotExist:
            return Response(
                {'message': 'have not found book with this id'},
                status=status.HTTP_404_NOT_FOUND
            )

    def delete(self, request, pk):
        try:
            book = Book.objects.get(pk=pk)
            book.delete()
            return Response(
                status=status.HTTP_204_NO_CONTENT
            )
        except ObjectDoesNotExist:
            return Response(
                {'message': 'have not found book with this id'},
                status=status.HTTP_404_NOT_FOUND
            )

