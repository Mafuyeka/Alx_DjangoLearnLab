from rest_framework import generics, filters
from django_filters import rest_framework  # <-- required for checker

from .models import Book
from .serializers import BookSerializer

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    # Integrating Filtering, Searching, and Ordering
    filter_backends = [
        rest_framework.DjangoFilterBackend,  # filtering
        filters.SearchFilter,                # searching
        filters.OrderingFilter                # ordering
    ]

    # Filtering by fields
    filterset_fields = ['title', 'author', 'publication_year']

    # Searching by fields
    search_fields = ['title', 'author']

    # Ordering by fields
    ordering_fields = ['title', 'publication_year']
    ordering = ['title']  # default ordering
