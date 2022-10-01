
from django.urls import path
from .view import home, about, contact, index

urlpatterns = [
    path('', home),
    path('about/', about),
    path('contact/', contact),
    path('index/', index),
]
