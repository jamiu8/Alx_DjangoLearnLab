This project uses Django REST Framework generic class-based views to efficiently handle CRUD operations on the Book model.

List View

View: BookListView

URL: /api/books/

Access: Public

Description: Returns a list of all books.

Detail View

View: BookDetailView

URL: /api/books/<int:pk>/

Access: Public

Description: Retrieve a specific book by ID.

Create View

View: BookCreateView

URL: /api/books/create/

Access: Authenticated Only

Description: Create a new book instance.

Custom Hook:

perform_create() for modifying data during creation.

Update View

View: BookUpdateView

URL: /api/books/<int:pk>/update/

Access: Authenticated Only

Description: Update an existing book.

Custom Hook:

perform_update() for data manipulation before saving.

Delete View

View: BookDeleteView

URL: /api/books/<int:pk>/delete/

Access: Authenticated Only

Description: Delete a book instance.

Permissions

Public read-only access for list and detail views.

Authentication required for create, update, and delete operations.

Powered by DRF’s built-in permission classes.