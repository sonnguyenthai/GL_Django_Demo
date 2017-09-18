"""gldemo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings

from .views.home import HomeView
from .views.add_book import AddBookView
from .views.edit_book import BookUpdate
from .views.remove_book import BookRemove

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^add-book$', AddBookView.as_view(), name='add_book'),
    url(r'^remove-book/(?P<pk>[0-9]+)/$', BookRemove.as_view(), name='remove_book'),
    url(r'^edit-book/(?P<pk>[0-9]+)/$', BookUpdate.as_view(), name='edit_book')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)