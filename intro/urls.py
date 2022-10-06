
from django.urls import path
#Import admin from django.contrib
from django.contrib import admin
#Import views from myapp
from myapp.views import index,home,about,contact,getProduct
urlpatterns = [
    path('admin/', admin.site.urls),   
    path('', index),
    #Get product
    path('getProduct/', getProduct),


]
