

# Create your views here.
from django.http import HttpResponse
from django.views import View


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")



class MyView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('Hello, World!')