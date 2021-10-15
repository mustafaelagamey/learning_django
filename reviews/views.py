from django.shortcuts import render
from .forms import ReviewForm, FeedbackForm


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


def feedback(request):
    if request.method == 'POST':
        feedback_form = FeedbackForm(request.POST)
        if feedback_form.is_valid():
            feedback_form.save()
            feedback_form = FeedbackForm()
    else :
        feedback_form = FeedbackForm()
    return render(request, 'reviews/feedback.html', {"feedback_form": feedback_form})
