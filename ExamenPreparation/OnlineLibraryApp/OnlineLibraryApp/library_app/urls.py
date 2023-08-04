from django.urls import path

from OnlineLibraryApp.library_app.views import index, add_book, edit_book, details_book, profile_page, profile_edit, \
    profile_delete, delete_book

urlpatterns = [
    path('', index, name='index'),
    path('add/book/', add_book, name='add-book'),
    path('edit/book/<int:pk>/', edit_book, name='edit-book'),
    path('delete/book/<int:pk>/', delete_book, name='delete-book'),
    path('details/book/<int:pk>/', details_book, name='details-book'),
    path('profile/', profile_page, name='profile-page'),
    path('profile/edit/', profile_edit, name='profile-edit'),
    path('profile/delete/', profile_delete, name='profile-delete'),

]