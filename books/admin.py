from .models import Book, Author
from django.contrib import admin


# Register your models here.

class BookAdmin(admin.ModelAdmin):
    # readonly_fields = ("slug",)
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ("rating",)
    list_display = ("title","rating")


admin.site.register(Book, BookAdmin)
admin.site.register(Author)
