from .models import Book
from django.contrib import admin


# Register your models here.

class BookAdmin(admin.ModelAdmin):
    readonly_fields = ("slug",)


admin.site.register(Book, BookAdmin)
