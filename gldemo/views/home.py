from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import TemplateView

from gldemo.models import Book


class HomeView(TemplateView):
    template_name = "gldemo/home.html"

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        all_books = Book.objects.order_by('-date_modified')
        paginator = Paginator(all_books, 4)  # Show 25 contacts per page

        page = self.request.GET.get('page')
        try:
            books = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            books = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            books = paginator.page(paginator.num_pages)
        context['books'] = books
        return context