
from django.urls import path
from django.http import HttpResponse


def home(request):
    print(request.method)
    r = HttpResponse('Hello World')
    return r
    

urlpatterns = [
    path('', home),
]
