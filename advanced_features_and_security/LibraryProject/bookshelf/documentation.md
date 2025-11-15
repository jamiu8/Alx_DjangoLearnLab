# Book Model Permissions

Permissions:
- can_view: Allows viewing a book
- can_create: Allows creating a book
- can_edit: Allows editing a book
- can_delete: Allows deleting a book

Groups:
- Viewers: can_view
- Editors: can_view, can_create, can_edit
- Admins: all permissions

Usage:
- Use @permission_required('yourapp.can_<action>', raise_exception=True) in views
- Assign users to groups via admin or script
