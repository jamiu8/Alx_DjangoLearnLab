from rest_framework import generics, filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django_filters import rest_framework as django_filters

from .models import Book
from .serializers import BookSerializer


class BookListView(generics.ListAPIView):
    """
    Enhanced Book ListView with:
    - Filtering
    - Searching
    - Ordering
    """

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    # Backends for filtering, search, and ordering
    filter_backends = [
        django_filters.DjangoFilterBackend,  # Filtering
        filters.SearchFilter,                # Searching
        filters.OrderingFilter               # Ordering
    ]

    # Fields allowed for filtering via ?field=value
    filterset_fields = ["title", "author", "publication_year"]

    # Fields allowed for searching via ?search=term
    search_fields = ["title", "author__name"]

    # Fields allowed for ordering via ?ordering=field
    ordering_fields = ["title", "publication_year"]

    # Default ordering
    ordering = ["title"]


class BookDetailView(generics.RetrieveAPIView):
    """
    Retrieve a single book by ID.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class BookCreateView(generics.CreateAPIView):
    """
    Create a new Book instance.
    Authenticated users only.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()


class BookUpdateView(generics.UpdateAPIView):
    """
    Update an existing Book instance.
    Authenticated users only.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    def perform_update(self, serializer):
        serializer.save()


class BookDeleteView(generics.DestroyAPIView):
    """
    Delete a Book instance.
    Authenticated users only.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
