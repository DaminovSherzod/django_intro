
from django.urls import path
from django.http import HttpResponse


def home(request):
    print(request.body)
    r = HttpResponse('Hello World')
    return r
    

urlpatterns = [
    path('', home),
]
