
from django.urls import path
from django.http import HttpResponse
from django.http import JsonResponse


def home(request):
    #Get query parameters
    a = request.GET.get('a')
    print(a)
    r = JsonResponse({'message': 'Hello World'})
    return r
    

urlpatterns = [
    path('', home),
]
