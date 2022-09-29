
from django.urls import path
from django.http import HttpResponse
from django.http import JsonResponse


def home(request):
    print(request.method)
    r = JsonResponse({'message': 'Hello World'})
    return r
    

urlpatterns = [
    path('', home),
]
