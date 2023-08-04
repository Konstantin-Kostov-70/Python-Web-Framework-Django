from django.urls import path

from Models_Demo.models_app.views import index, delete_students, students_details, university_details

urlpatterns = [
    path('', index, name='home'),
    path('delete/<int:pk>', delete_students, name='delete'),
    path('details/<int:pk>', students_details, name='details'),
    path('uni-details/<int:pk>/<slug:slug>/', university_details, name='uni-details'),
]
