from django.urls import path
from .views import UploadFileView, UploadFileViaFormView

app_name = 'filesuploader'

urlpatterns = [
    path('upload', UploadFileView.as_view(), name='upload'),
    path('upload-via-django-form', UploadFileViaFormView.as_view(), name='upload-via-django-form'),
]
