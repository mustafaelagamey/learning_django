from django.urls import path
from .views import review, feedback, ReviewView, ThankYouView, FeedbackListView

app_name = 'reviews'

urlpatterns = [
    path('', review, name='add-review'),
    path('class-based-view-review', ReviewView.as_view(), name='add-class-based-view-review'),
    path('feedback', feedback, name='add-feedback'),
    path('thank-you', ThankYouView.as_view(), name='thank-you'),
    path('list-feedbacks', FeedbackListView.as_view(), name='list-feedbacks'),
]
