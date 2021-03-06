from django.db.models.functions import Length
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from .forms import ReviewForm, FeedbackForm
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, FormView, CreateView
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


class ReviewFormView(FormView):
    form_class = ReviewForm
    template_name = 'reviews/review.html'
    success_url = reverse_lazy('reviews:thank-you')

    def form_valid(self, form):
        # send email
        return super(ReviewFormView, self).form_valid(form)


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
    return render(request, 'reviews/feedback.html', {"form": feedback_form})


class FeedbackCreateView(CreateView):
    model = Feedback
    fields = '__all__'

    template_name = 'reviews/feedback.html'
    success_url = reverse_lazy('reviews:thank-you')


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

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(FeedbackListView, self).get_context_data()
        context["session_favourite_review"] = self.request.session.get("session_favourite_review")
        return context

    def get_queryset(self):
        query_set = super(FeedbackListView, self).get_queryset()
        # returns only usernames more than 2
        return query_set.annotate(user_name_len=Length('user_name')).filter(user_name_len__gt=2)


class FeedbackDetailView(DetailView):
    model = Feedback
    template_name = 'reviews/feedback_detail.html'

    def get_context_data(self, **kwargs):
        context = super(FeedbackDetailView, self).get_context_data(**kwargs)
        context["is_session_favourite"] = self.request.session.get("session_favourite_review") == self.object.pk
        return context





class SessionFavFeedback(View):
    def post(self, request, pk):
        request.session["session_favourite_review"] = pk
        return redirect('reviews:feedback-detail', pk=pk)
