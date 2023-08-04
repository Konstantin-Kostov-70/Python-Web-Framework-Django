from django.urls import path
from Urls_and_Views.department.views import index, sample_view

urlpatterns = [
   path('', index, name='index'),
   path('sample/<int:department_id>', sample_view, name='sample'),
]