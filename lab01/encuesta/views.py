from django.shortcuts import render
from django.http import response 

# Create your views here.

def pagina (request,*cadena,**cadenaI): 
    return render (request, 'encuesta/ejemplo.html')