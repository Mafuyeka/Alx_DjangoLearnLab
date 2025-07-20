from django.urls import path
from .views import list_all_books, LibraryDetailView, add_book, edit_book, delete_book

urlpatterns = [
    path('books/', list_all_books, name='list_all_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    path('add_book/', add_book, name='add_book'),
    path('edit_book/<int:pk>/', edit_book, name='edit_book'),
    path('delete_book/<int:pk>/', delete_book, name='delete_book'),
]
