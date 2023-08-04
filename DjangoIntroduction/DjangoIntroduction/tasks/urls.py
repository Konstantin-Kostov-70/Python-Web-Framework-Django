from django.urls import path
from DjangoIntroduction.tasks.views import index, get_all_tasks

urlpatterns = [
    path('', index, name='index'),
    path('all/', get_all_tasks, name='all')
]