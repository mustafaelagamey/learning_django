from django.urls import path

from . import views
# Urls for this app
urlpatterns = [
    path("", views.index),
    path("<int:month>", views.month_challenge_by_number),
    path("<str:month>", views.month_challenge),

]
