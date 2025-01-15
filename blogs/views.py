from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def posts(request):
    return HttpResponse("<h1> You will get the posts soon </h1> ")
def home(req): 
    return HttpResponse("this is profile page")