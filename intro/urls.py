
from django.urls import path
from django.http import HttpResponse


def home(x):
    print('HOME')
    r = HttpResponse('Hello World')
    return r
    

urlpatterns = [
    path('', home),
]
