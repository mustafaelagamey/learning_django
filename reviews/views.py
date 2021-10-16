from django.shortcuts import render, redirect
from .forms import ReviewForm, FeedbackForm
from django.views import View
from django.views.generic import TemplateView


class ReviewView(View):
    def get(self, request):
        form = ReviewForm()
        return render(request, 'reviews/review.html', {"form": form})

    def post(self, request):
        form = ReviewForm(request.POST)
        if form.is_valid():
            # send email
            return redirect('reviews:thank-you')

        return render(request, 'reviews/review.html', {"form": form})


# Create your views here.
def review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            # send email
            return redirect('reviews:thank-you')
    else:
        form = ReviewForm()
    return render(request, 'reviews/review.html', {"form": form})


def feedback(request):
    if request.method == 'POST':
        feedback_form = FeedbackForm(request.POST)
        if feedback_form.is_valid():
            feedback_form.save()
            feedback_form = FeedbackForm()
    else:
        feedback_form = FeedbackForm()
    return render(request, 'reviews/feedback.html', {"feedback_form": feedback_form})


class ThankYouView(TemplateView):
    template_name = 'reviews/thank-you.html'
