
from django.urls import path
from myapp.views import index, home, about, contact
urlpatterns = [
    path('', home),
    path('about/', about),
    path('contact/', contact),
    path('index/', index),
]
