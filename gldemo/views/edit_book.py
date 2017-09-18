from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView

from gldemo.models import Book
from gldemo.forms import BookForm


class BookUpdate(SuccessMessageMixin, UpdateView):
    model = Book
    form_class = BookForm
    template_name = 'gldemo/add_book.html'
    success_url = reverse_lazy("home")
    success_message = "The book %(book_name)s was updated successfully"

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(cleaned_data,
                                           book_name=self.object.name)