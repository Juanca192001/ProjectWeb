from django.shortcuts import render
from .models import Coche, Marca, Modelo

def home(request):
    coches = Coche.objects.all()
    marcas = Marca.objects.all()
    modelos = Modelo.objects.all()
    return render(request, 'ProyectoWeb/home.html', {'coches': coches, 'marcas': marcas, 'modelos': modelos})

def login_view(request):
    return render(request, 'ProyectoWeb/login.html')
