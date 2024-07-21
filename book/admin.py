from django.contrib import admin
from .models import Book, BookQuantity
# Register your models here.

admin.site.register(Book)
admin.site.register(BookQuantity)