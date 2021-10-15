from django.urls import path
from .views import review, feedback

app_name = 'reviews'

urlpatterns = [
    path('', review, name='add-review'),
    path('feedback', feedback, name='add-feedback')
]
