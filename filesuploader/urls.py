from django.urls import path
from .views import UploadFileView, UploadFileViaFormView, UploadFileViaModel, UploadFileCreateView, UploadFileListView

app_name = 'filesuploader'

urlpatterns = [
    path('upload', UploadFileView.as_view(), name='upload'),
    path('upload-via-django-form', UploadFileViaFormView.as_view(), name='upload-via-django-form'),
    path('upload-via-django-model', UploadFileViaModel.as_view(), name='upload-via-django-model'),
    path('upload-via-django-create-view', UploadFileCreateView.as_view(), name='upload-via-django-create-view'),
    path('list-uploaded-files', UploadFileListView.as_view(), name='list-uploaded-files'),
]
