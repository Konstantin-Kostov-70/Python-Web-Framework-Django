from django.urls import path, include

from GamePlayApp.game_app.views import index, dashboard, profile_create, \
    profile_edit, profile_details, profile_delete, \
    game_create, game_edit, game_details, game_delete

urlpatterns = [
    path('', index, name='index'),
    path('dashboard/', dashboard, name='dashboard'),
    path('profile/', include([
        path('create/', profile_create, name='profile-create'),
        path('edit/', profile_edit, name='profile-edit'),
        path('details/', profile_details, name='profile-details'),
        path('delete/', profile_delete, name='profile-delete'),
    ])),
    path('game/', include([
        path('create/', game_create, name='game-create'),
        path('edit/<int:pk>/', game_edit, name='game-edit'),
        path('details/<int:pk>/', game_details, name='game-details'),
        path('delete/<int:pk>/', game_delete, name='game-delete'),
    ]))
]
