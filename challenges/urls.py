from django.urls import path

from . import views
# Urls for this app
urlpatterns = [
    path("", views.index),
    path("january", views.jan),
]