
from django.shortcuts import render
from .models import Coche

def home(request):
    coches = Coche.objects.all()
    return render(request, 'ProyectoWeb/home.html', {'coches': coches})

def login_view(request):
    return render(request, 'ProyectoWeb/login.html')
