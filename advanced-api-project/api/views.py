from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer
# Create your views here.

class BookListView(generics.ListAPIView):
    """
    BookListView
    -------------
    Retrieves a list of all books in the system.
    
    - No authentication required (Read-Only).
    - Uses ListAPIView for efficient querying.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]  # Public read access


class BookDetailView(generics.RetrieveAPIView):
    """
    BookDetailView
    ----------------
    Retrieves a single book by its ID (pk).
    
    - No authentication required for read access.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]


class BookCreateView(generics.CreateAPIView):
    """
    BookCreateView
    ----------------
    Creates a new Book instance.
    
    Custom Behavior:
    - Only authenticated users may create books.
    - Validation is handled by BookSerializer (including future-year check).
    - Can be extended using perform_create() to attach current user if needed.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        """
        Hook to modify behavior during object creation.
        
        Example use case:
        - Attach the user who created the book.
        - Clean or modify data before saving.
        """
        serializer.save()


class BookUpdateView(generics.UpdateAPIView):
    """
    BookUpdateView
    ----------------
    Updates an existing Book instance.
    
    - Only authenticated users may update data.
    - Uses UpdateAPIView which automatically handles PATCH/PUT.
    - Behaviors can be customized with perform_update().
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_update(self, serializer):
        """
        Custom hook to modify data before saving updates.
        """
        serializer.save()


class BookDeleteView(generics.DestroyAPIView):
    """
    BookDeleteView
    ----------------
    Deletes a Book instance.
    
    - Only authenticated users may delete.
    - Uses DestroyAPIView for clean delete behavior.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]