from django.contrib import admin
from .models import Book

# Register your models here.

class Bookadmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_date')
    search_fields = ('title', 'author', 'publication_date')
    list_filter = ('title', 'author', 'publication_date')

admin.site.register(Book)
