from books.models import Book
from django.db.models import Avg
from django.shortcuts import render

# Create your views here.


def listing(request):
    books = Book.objects.all()
    count = Book.objects.count()
    avg_rating = books.aggregate(Avg("rating"))
    context = {
        'books': books,
        'count': count,
        'avg_rating':avg_rating['rating__avg']
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
