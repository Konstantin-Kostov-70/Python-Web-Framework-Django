from django.urls import path

from NotesApp.notes_app.views import index, add_note, edit_note, delete_note, details_note, profile, delete_profile

urlpatterns = [
    path('', index, name='index'),
    path('add/', add_note, name='add'),
    path('edit/<int:pk>/', edit_note, name='edit'),
    path('delete/<int:pk>/', delete_note, name='delete'),
    path('details/<int:pk>/', details_note, name='details'),
    path('profile/', profile, name='profile'),
    path('profile/delete/', delete_profile, name='profile-delete')
]