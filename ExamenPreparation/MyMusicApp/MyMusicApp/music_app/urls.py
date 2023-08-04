from django.urls import path, include

from MyMusicApp.music_app.views import home, album_add, album_details, \
    album_edit, album_delete, profile_details, profile_delete

urlpatterns = [
    path('', home, name='home'),
    path('album/', include([
        path('add', album_add, name='album-add'),
        path('details/<int:pk>', album_details, name='album-details'),
        path('edit/<int:pk>', album_edit, name='album-edit'),
        path('delete/<int:pk>', album_delete, name='album-delete'),
    ])),
    path('profile/', include([
        path('details', profile_details, name='profile-details'),
        path('delete/', profile_delete, name='profile-delete'),
    ]))
]