from rest_framework import serializers
from datetime import datetime
from .models import Author, Book


class BookSerializer(serializers.ModelSerializer):
    """
    BookSerializer
    --------------
    Serializes all fields of the Book model.
    
    Includes custom validation:
    - publication_year must not be in the future.
    """

    class Meta:
        model = Book
        fields = "__all__"

    def validate_publication_year(self, value):
        """
        Validate that publication_year is not greater than the current year.
        """
        current_year = datetime.now().year
        if value > current_year:
            raise serializers.ValidationError(
                "Publication year cannot be in the future."
            )
        return value


class AuthorSerializer(serializers.ModelSerializer):
    """
    AuthorSerializer
    ----------------
    Serializes the Author model.
    
    Includes:
    - name: The author’s name.
    - books: Nested serialization of all related books using BookSerializer.
    
    The relationship:
    - The 'books' field is populated from the 'related_name' in the Book model.
      That is, Book.author → Author.books
    """
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ["name", "books"]
