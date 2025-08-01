# Retrieve Book Instance

from bookshelf.models import Book

# Retrieve and display all attributes of the book you just created
book = Book.objects.get(title="1984")
print(book.title, book.author, book.publication_year)
