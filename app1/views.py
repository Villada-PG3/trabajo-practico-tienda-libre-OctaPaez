from django.shortcuts import render
from django.http import HttpResponse

def hello_world(request):
    return render(request, "hola.html")
# Create your views here.
