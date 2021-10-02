from books.models import Book
from django.shortcuts import render

# Create your views here.


def listing(request):
    books = Book.objects.all()
    count = Book.objects.count()
    context = {
        'books': books,
        'count': count,
    }
    return render(request, 'books/listing.html',context=context)


def detail(request, slug):
    try:
        book = Book.objects.get(slug=slug)
    except Book.DoesNotExist:
        book = None
    context = {
        'book': book
    }
    return render(request, 'books/detail.html', context=context)
