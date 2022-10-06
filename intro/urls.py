
from django.urls import path
from myapp.views import index, home, about, contact
from django.contrib import admin
urlpatterns = [
    path('admin/',admin.site.urls),
    path('', home),
    path('about/', about),
    path('contact/', contact),
    path('index/', index),
]
