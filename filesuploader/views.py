from django.shortcuts import render

# Create your views here.
from django.views import View


class UploadFileView(View):

    def get(self, request):
        return render(request, 'filesuploader/upload.html')

    def post(self, request):
        pass
