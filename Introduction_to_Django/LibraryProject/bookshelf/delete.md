### **`delete.md`**
```markdown
# Delete Operation

```python
from bookshelf.models import Book

# Delete the book
book = Book.objects.first()
book.delete()  # (1, {'bookshelf.Book': 1})

# Confirm deletion
Book.objects.all()  # <QuerySet []>