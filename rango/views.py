from django.http import HttpResponse
from httplib import HTTPResponse

def index(request):
    return HttpResponse("Rango says hello world!")

def about(request):
    return HTTPResponse("Rango Says: Here is the about page <a href='/rango/about'>About</a>")
