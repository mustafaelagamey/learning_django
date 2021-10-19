from django.urls import path
from .views import review, feedback, ReviewView, ThankYouView, FeedbackListView, FeedbackDetailView, ReviewFormView, \
    FeedbackCreateView, SessionFavFeedback

app_name = 'reviews'

urlpatterns = [
    path('', review, name='add-review'),
    path('class-based-view-review', ReviewView.as_view(), name='add-class-based-view-review'),
    path('form-view-review', ReviewFormView.as_view(), name='add-form-view-review'),
    path('feedback', feedback, name='add-feedback'),
    path('create-view-feedback', FeedbackCreateView.as_view(), name='add-create-view-feedback'),
    path('thank-you', ThankYouView.as_view(), name='thank-you'),
    path('list-feedbacks', FeedbackListView.as_view(), name='list-feedbacks'),
    path('feedback-detail/<int:pk>', FeedbackDetailView.as_view(), name='feedback-detail'),
    path('session-fav-feedback/<int:pk>', SessionFavFeedback.as_view(), name='session-fav-feedback'),
]
