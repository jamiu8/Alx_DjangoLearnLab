from relationship_app.models import Book, Library, Librarian

Book.objects.filter(author = "salmon")

books = Library.objects.get(name="library_name")
books.book.all()

# Library.objects.values_list("book", flat=True)

Libr = Library.objects.get(name="library_name")

Libr.book.all()

