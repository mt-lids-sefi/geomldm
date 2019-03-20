# Create your views here.
from django.http import HttpResponse
from django.views import View
from mapfiles.models import Document
from mapfiles.forms import DocumentForm
from django.shortcuts import render, redirect

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = DocumentForm()
    return render(request, 'model_form_upload.html', {
        'form': form
    })


class MyView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('Hello, World!')

