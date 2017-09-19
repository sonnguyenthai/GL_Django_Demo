from django.contrib import admin

from .models import Book


class BookAdmin(admin.ModelAdmin):
    list_display = ('name', 'author', 'date_published')

admin.site.register(Book, BookAdmin)
