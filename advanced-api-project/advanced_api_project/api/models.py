from django.db import models
from datetime import datetime
# Create your models here.


class Author(models.Model):
    """
    Author Model
    ------------
    Represents a writer in the system.

    Fields:
    - name: Stores the full name of the author.
    - books: (reverse relation) Represents all books written by the author.
             Created automatically from the Book model's foreign key via 'related_name'.
    """
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Book(models.Model):
    """
    Book Model
    ----------
    Represents a book written by an author.

    Fields:
    - title: Title of the book.
    - publication_year: Year the book was published.
    - author: ForeignKey that creates a One-to-Many relationship between Author → Books.
              Each book belongs to one author, but an author can have many books.
    """
    title = models.CharField(max_length=255)
    publication_year = models.IntegerField()
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        related_name="books"   # Enables author.books to access all related books
    )

    def __str__(self):
        return self.title
