from books.models import Book
from django.shortcuts import render

# Create your views here.


def listing(request):
    books = Book.objects.all()
    context = {
        'books' :books
    }
    return render(request, 'books/listing.html',context=context)
