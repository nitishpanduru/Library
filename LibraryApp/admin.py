from django.contrib import admin
from .models import Book,IssuedItem
# Register your models here.

admin.site.register(Book)
admin.site.register(IssuedItem)
