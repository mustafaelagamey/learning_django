from books.models import Book
from django.shortcuts import render

# Create your views here.


def listing(request):
    books = Book.objects.all()
    context = {
        'books' :books
    }
    return render(request, 'books/listing.html',context=context)


def detail(request, id):
    try:
        book = Book.objects.get(id=id)
    except Book.DoesNotExist:
        book = None
    context = {
        'book': book
    }
    return render(request, 'books/detail.html', context=context)
