from django.views.generic.edit import CreateView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy

from gldemo.models import Book
from gldemo.forms import BookForm


class AddBookView(SuccessMessageMixin, CreateView):
    model = Book
    form_class = BookForm
    # fields = ['name', 'author', 'date_published', 'book_cover_image', 'description', 'book_url']
    template_name = "gldemo/add_book.html"
    success_url = reverse_lazy("home")
    success_message = "The book %(book_name)s was added successfully"

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(cleaned_data,
                                           book_name=self.object.name)
