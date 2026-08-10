from django.shortcuts import render
from django.http import HttpResponse

def hello_world(request):
    return render(request, "hola.html")
# Create your views here.

def home(request):
    return render(request, "app1/home.html")

def acerca_de_mi(request):
    return render(request, 'app1/acerca-de-mi.html')