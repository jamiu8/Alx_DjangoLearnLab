
---

### **`retrieve.md`**
```markdown
# Retrieve Operation

```python
from bookshelf.models import Book

# Retrieve all books
books = Book.objects.all()
books  # <QuerySet [<Book: 1984 by George Orwell (1949)>]>

# Retrieve individual attributes
 books = Book.objects.get(id = 1)
book.title, book.author, book.publication_year  # ('1984', 'George Orwell', 1949)
