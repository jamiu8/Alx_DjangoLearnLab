from relationship_app.models import Book, Library, Librarian

Book.objects.filter(author = "salmon")

Library.objects.values_list("book", flat=True)

Librarian.objects.all()

