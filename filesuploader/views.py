from django.shortcuts import render, redirect

# Create your views here.
from django.views import View
from filesuploader.forms import FileUploadForm


def store_file(file):
    import os
    os.makedirs("temp", exist_ok=True)
    with open(f"temp/{file}", "wb+") as dest:
        for chunk in file.chunks():
            dest.write(chunk)


class UploadFileView(View):

    def get(self, request):
        return render(request, 'filesuploader/upload.html')

    def post(self, request):
        store_file(request.FILES['file'])
        return redirect('filesuploader:upload')


class UploadFileViaFormView(View):

    def get(self, request):
        return render(request, 'filesuploader/upload-via-django-form.html', {'form': FileUploadForm()})

    def post(self, request):
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            store_file(request.FILES['file'])
            return redirect('filesuploader:upload-via-django-form')

        else:
            return render(request, 'filesuploader/upload-via-django-form.html', {'form': form})
