from django.http import HttpResponse

# Create your views here.

def home(request :any , name):
    return HttpResponse('Hello World  ' + name)
