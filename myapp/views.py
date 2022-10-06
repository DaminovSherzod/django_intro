from django.http import HttpResponse
from django.http import JsonResponse
from .models import Person

def home(request):
     person = Person.objects.all()
     users = {'results':[]}

     for p in person:
          data = {}
          data['id']=p.id
          data['first_name']=p.first_name
          data['last_name']=p.last_name 
          users['results'].append(data)
     return JsonResponse(users)


     


    

