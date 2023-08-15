from django.urls import path, include

from Car.car_app.views import index, catalog, profile_create, profile_details, profile_edit, profile_delete, car_create, \
    car_details, car_edit, car_delete

urlpatterns = [
    path('', index, name='index'),
    path('catalog/', catalog, name='catalog'),
    path('profile/', include([
        path('create/', profile_create, name='profile-create'),
        path('details/', profile_details, name='profile-details'),
        path('edit/', profile_edit, name='profile-edit'),
        path('delete/', profile_delete, name='profile-delete'),
    ])),
    path('car/', include([
        path('create/', car_create, name='car-create'),
        path('details/<int:pk>/', car_details, name='car-details'),
        path('edit/<int:pk>/', car_edit, name='car-edit'),
        path('delete/<int:pk>/', car_delete, name='car-delete'),
    ])),
]

