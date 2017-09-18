from django.forms import ModelForm

from .models import Book


class BookForm(ModelForm):
    class Meta:
        model = Book
        exclude = ('date_created', 'date_modified')