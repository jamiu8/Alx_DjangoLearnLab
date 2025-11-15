from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import EmailUser

# Register your models here.

class CustomUserAdmin(UserAdmin):
    # Fields to display in the admin list view
    list_display = ('email', 'username', 'dob', 'dp', 'phone', 'is_staff', 'is_superuser', 'is_active')
    
    # Fields you can filter by in the admin sidebar
    list_filter = ('is_staff', 'is_superuser', 'is_active')
    
    # Fields to show when editing a user
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('username', 'dp', 'dob', )}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    
    # Fields to show when creating a new user
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'dob', 'dp', 'password1', 'password2', 'is_staff', 'is_superuser', 'is_active')}
        ),
    )
    
    # Enable search by email or name
    search_fields = ('email', 'first_name', 'last_name')
    
    # Default ordering in admin list view
    ordering = ('email',)
    
    # Enable filter by groups
    filter_horizontal = ('groups', 'user_permissions',)
