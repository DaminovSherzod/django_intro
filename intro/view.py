from django.http import HttpResponse

def index(request):
  
    return HttpResponse("<h1>Index</h1>")

def home(request):
      
     return HttpResponse("<h1>Home</h1>")

def about(request):
      
     return HttpResponse("<h1>About</h1>")  

def contact(request): 
    return HttpResponse("<h1>Contact</h1>")

def services(request):
    return HttpResponse("<h1>Services</h1>")

def blog(request):
    return HttpResponse("<h1>Blog</h1>")

def portfolio(request):
    return HttpResponse("<h1>Portfolio</h1>")

def team(request):
    return HttpResponse("<h1>Team</h1>")

def faq(request):
    return HttpResponse("<h1>FAQ</h1>")

def error(request):
    return HttpResponse("<h1>Error</h1>")


    

