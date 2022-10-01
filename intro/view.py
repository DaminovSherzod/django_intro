from django.http import HttpResponse

def home(request):
    #Get query parameters
    a = request.GET.get('a')
    print(a)
    r = HttpResponse('HOME')
    return r
    

