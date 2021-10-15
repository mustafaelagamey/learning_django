from django.urls import path
from .views import review

app_name = 'reviews'

urlpatterns = [
    path('', review, name='add-review')
]
