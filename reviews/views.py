from django.shortcuts import render
from .forms import ReviewForm


# Create your views here.
def review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            # send email
            return render(request, 'reviews/thank-you.html', {'form': form.cleaned_data})
    else:
        form = ReviewForm()
    return render(request, 'reviews/review.html', {"form": form})
