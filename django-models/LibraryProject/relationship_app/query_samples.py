from relationship_app.models import Book, Library, Librarian, Author

authe = Author.objects.get(name=author_name)
    authe.objects.filter(author=author)


book = Library.objects.get(name=library_name)
book.books.all()

# Library.objects.values_list("book", flat=True)

Libr = Library.objects.get(name="library_name")


