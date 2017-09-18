from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView

from gldemo.models import Book


class BookRemove(DeleteView):
    model = Book
    success_url = reverse_lazy('home')
    template_name = "gldemo/book_confirm_remove.html"
    success_message = "The book %(book_name)s was updated successfully"

    def delete(self, request, *args, **kwargs):
        response = super(BookRemove, self).delete(request, *args, **kwargs)
        success_message = self.success_message % dict(book_name=self.object.name)
        if success_message:
            messages.success(self.request, success_message)
        return response
