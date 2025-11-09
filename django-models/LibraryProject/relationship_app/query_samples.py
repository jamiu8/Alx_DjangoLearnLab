from relationship_app.models import Book, Library, Librarian

Book.objects.filter(author = "salmon")

book = Library.objects.get(name= library_name)
book.books.all()

# Library.objects.values_list("book", flat=True)

Libr = Library.objects.get(name="library_name")


