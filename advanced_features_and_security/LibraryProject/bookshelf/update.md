
---

### **`update.md`**
```markdown
# Update Operation

```python
from bookshelf.models import Book

# Update the title of the book
book = Book.objects.first()
book.title = "Nineteen Eighty-Four"
book.save()
book  # <Book: Nineteen Eighty-Four by George Orwell (1949)>
