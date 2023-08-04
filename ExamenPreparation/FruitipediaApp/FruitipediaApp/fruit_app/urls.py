from django.urls import path, include

from FruitipediaApp.fruit_app.views import index, dashboard, \
    profile_create, profile_details, profile_edit, profile_delete,\
    fruit_create, fruit_details, fruit_edit, fruit_delete

urlpatterns = [
    path('', index, name='index'),
    path('dashboard/', dashboard, name='dashboard'),
    path('profile/', include([
        path('create/', profile_create, name='profile-create'),
        path('details/', profile_details, name='profile-details'),
        path('edit/', profile_edit, name='profile-edit'),
        path('delete/', profile_delete, name='profile-delete'),
    ])),
    path('fruit/', include([
        path('create/', fruit_create, name='fruit-create'),
        path('details/<int:pk>/', fruit_details, name='fruit-details'),
        path('edit/<int:pk>/', fruit_edit, name='fruit-edit'),
        path('delete/<int:pk>/', fruit_delete, name='fruit-delete'),
    ])),
]