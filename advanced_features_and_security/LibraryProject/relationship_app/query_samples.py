from relationship_app.models import Book, Library, Librarian, Author

authe = Author.objects.get(name='')
authe.objects.filter(author="author")


book = Library.objects.get(name='')
book.books.all()

# Library.objects.values_list("book", flat=True)S

Librarian.objects.get(library= "s")

