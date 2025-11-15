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


# SECURITY CONFIGURATIONS
# DEBUG=False: Never expose debug info in production
# SECURE_BROWSER_XSS_FILTER=True: Enables browser XSS filter
# X_FRAME_OPTIONS='DENY': Prevents clickjacking
# CSRF_COOKIE_SECURE=True: Ensures CSRF cookie is only sent over HTTPS
# SESSION_COOKIE_SECURE=True: Ensures session cookie is only sent over HTTPS
# CSP settings: Restrict scripts, styles, and images to trusted sources
