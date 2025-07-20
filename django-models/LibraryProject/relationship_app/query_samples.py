from django.core.exceptions import ObjectDoesNotExist
from .models import Author, Book, Library, Librarian

def list_books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        return library.books.all()  # assuming related_name='books' in Book model's FK to Library
    except ObjectDoesNotExist:
        return Book.objects.none()

def books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)
        return Book.objects.filter(author=author)
    except ObjectDoesNotExist:
        return Book.objects.none()

def get_librarian_for_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        return getattr(library, 'librarian', None)
    except ObjectDoesNotExist:
        return None
