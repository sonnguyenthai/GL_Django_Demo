from django.db import models


class Book(models.Model):
    name = models.CharField(max_length=200, null=False, verbose_name="Book Title")
    author = models.CharField(max_length=100, null=False, default='', verbose_name="Author")
    description = models.TextField(null=False, default="", verbose_name="Description")
    date_published = models.DateField(null=True, verbose_name="Published Date")
    book_cover_image = models.ImageField(verbose_name="Cover Photo", null=False, upload_to='books', default='')
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)