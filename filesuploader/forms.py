from django import forms
from filesuploader.models import FileUploadModel


class FileUploadForm(forms.Form):
    file = forms.FileField()


class FileUploadModelForm(forms.ModelForm):
    class Meta:
        model = FileUploadModel
        fields = ['file']
