from .models import Book, Author, Address
from django.contrib import admin


# Register your models here.

class AuthorAdmin(admin.ModelAdmin):
    list_display = ("__str__", "first_name", "last_name")


class BookAdmin(admin.ModelAdmin):
    # readonly_fields = ("slug",)
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ("rating",)
    list_display = ("title", "rating", "author")


admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Address)
