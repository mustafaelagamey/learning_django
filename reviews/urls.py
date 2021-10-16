from django.urls import path
from .views import review, feedback, ReviewView

app_name = 'reviews'

urlpatterns = [
    path('', review, name='add-review'),
    path('class-based-view-review', ReviewView.as_view(), name='add-class-based-view-review'),
    path('feedback', feedback, name='add-feedback')
]
