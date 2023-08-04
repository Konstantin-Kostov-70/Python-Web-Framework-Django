from django.urls import path

from DjangoRESTDemo.demo_api.views import BookListCreateView, BookGetPutDelete

urlpatterns = [
    path('books/', BookListCreateView.as_view(), name='books'),
    path('books/<int:pk>/', BookGetPutDelete.as_view(), name='simple-book')
]