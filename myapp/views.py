from django.http import HttpResponse
from django.http import JsonResponse
from .models import Product

def getProduct(request):

     #Get the list of products from the database
     products = Product.objects.all()
     #Create a list of dictionaries
     products_list = []
     #Loop through the products
     for product in products:
           #Create a dictionary
           product_dict = {}
           #Add the fields to the dictionary
           product_dict['title'] = product.title
           product_dict['description'] = product.description
           product_dict['price'] = product.price
           #Add the dictionary to the list
           products_list.append(product_dict)
     return JsonResponse(products_list,safe=False)

def index(request):


     
     
    return HttpResponse("<h1>Index</h1><h3>Index page</h3>")

def home(request):
     #Get the value of the post request
     name = request.POST
     print(name)  
     return HttpResponse("<h1>Home</h1>")

def about(request):
      
     return HttpResponse("<h1>About</h1>")  

def contact(request): 
    return HttpResponse("<h1>Contact</h1>")



    

