from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("Hello from dipendra Tamang, its keep on testing \n this website is being developed by dipendra using python django ")