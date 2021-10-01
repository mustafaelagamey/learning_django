from django.urls import path
from .views import listing

app_name = 'books'
urlpatterns = [
    path('listing', listing, name='listing')
]
