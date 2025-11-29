from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .models import Book
from .serializers import BookSerializer
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters import rest_framework as filters
# Create your views here.

class BookListView(generics.ListAPIView):
    """
    Enhanced Book List endpoint with:
    - Filtering
    - Searching
    - Ordering
    """

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    # Filter, Search, and Ordering backends
    filter_backends = [filters.DjangoFilterBackend, SearchFilter, OrderingFilter]

    # Filtering fields
    filterset_fields = ["title", "author", "publication_year"]

    # Search fields
    search_fields = ["title", "author__name"]

    # Ordering fields
    ordering_fields = ["title", "publication_year"]

    # Optional default ordering
    ordering = ["title"]



class BookDetailView(generics.RetrieveAPIView):
    """
    Retrieve a single book by ID.
    Public access allowed.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class BookCreateView(generics.CreateAPIView):
    """
    Create a new book.
    Only authenticated users may create.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Explicit import

    def perform_create(self, serializer):
        serializer.save()


class BookUpdateView(generics.UpdateAPIView):
    """
    Update an existing book.
    Only authenticated users may update.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    def perform_update(self, serializer):
        serializer.save()


class BookDeleteView(generics.DestroyAPIView):
    """
    Delete a book.
    Only authenticated users may delete.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

class BookFilter(filters.FilterSet):
    order_by = filters.OrderingFilter(
        fields=(
            ("title", "title"),
            ("published_date", "published_date"),
        )
    )

    class Meta:
        model = Book
        fields = ["title", "author"]
