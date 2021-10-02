from .models import Book
from django.contrib import admin


# Register your models here.

class BookAdmin(admin.ModelAdmin):
    pass


admin.site.register(Book, BookAdmin)
