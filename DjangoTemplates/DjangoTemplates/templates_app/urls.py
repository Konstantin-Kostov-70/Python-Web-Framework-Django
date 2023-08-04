from django.urls import path

from DjangoTemplates.templates_app.views import index, get_students, get_values, get_articles

urlpatterns = [
    path('', index, name='index'),
    path('students/', get_students, name='students'),
    path('values/', get_values, name='values'),
    path('articles/', get_articles, name='show-articles')
]