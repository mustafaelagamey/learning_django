from django.db.models.functions import Length
from django.shortcuts import render, redirect
from .forms import ReviewForm, FeedbackForm
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView
from .models import Feedback


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
            return redirect('reviews:thank-you')
    else:
        feedback_form = FeedbackForm()
    return render(request, 'reviews/feedback.html', {"feedback_form": feedback_form})


class ThankYouView(TemplateView):
    template_name = 'reviews/thank-you.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["user_name"] = "Dear Customer"
        return context


class FeedbackListView(ListView):
    model = Feedback
    template_name = 'reviews/feedback_list.html'
    context_object_name = 'feedbacks'

    def get_queryset(self):
        query_set = super(FeedbackListView, self).get_queryset()
        # returns only usernames more than 2
        return query_set.annotate(user_name_len=Length('user_name')).filter(user_name_len__gt=2)


class FeedbackDetailView(DetailView):
    model = Feedback
    template_name = 'reviews/feedback_detail.html'
