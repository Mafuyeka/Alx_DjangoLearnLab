from .models import Author, Book, Library, Librarian

def list_books_in_library(library_name):
    library = Library.objects.filter(name=library_name).first()
    if library:
        return library.books.all()
    return Book.objects.none()


def books_by_author(author_name):
    author = Author.objects.filter(name=author_name).first()
    if author:
        return Book.objects.filter(author=author)
    return Book.objects.none()


def get_librarian_for_library(library_name):
    library = Library.objects.filter(name=library_name).first()
    if library:
        return getattr(library, 'librarian', None)
    return None
