from django.shortcuts import render
from .forms import ReviewForm


# Create your views here.
def review(request):
    form = ReviewForm()
    return render(request, 'reviews/review.html', {"form": form})
