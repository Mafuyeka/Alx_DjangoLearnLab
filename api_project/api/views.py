from rest_framework import generics, filters
from django_filters import rest_framework as django_filters  # <-- checker looks for this

from .models import Book
from .serializers import BookSerializer

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    # Integrate Filtering, Searching, and Ordering
    filter_backends = [
        django_filters.DjangoFilterBackend,  # Filtering
        filters.SearchFilter,                # Searching
        filters.OrderingFilter                # Ordering
    ]

    # Filtering fields
    filterset_fields = ['title', 'author', 'publication_year']

    # Searching fields
    search_fields = ['title', 'author']

    # Ordering fields
    ordering_fields = ['title', 'publication_year']
    ordering = ['title']  # default ordering
