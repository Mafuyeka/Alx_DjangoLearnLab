# Delete Book Instance

```python
from bookshelf.models import Book

# Delete the book instance
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()

# Confirm deletion by listing all books
print(Book.objects.all())
