from django.urls import path
from .views import listing, detail

app_name = 'books'
urlpatterns = [
    path('listing', listing, name='listing'),
    path('detail/<slug>', detail, name='detail'),
]
