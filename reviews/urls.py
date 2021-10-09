from django.urls import path
from .views import review

app_name = 'books'

urlpatterns = [
    path('', review)
]
