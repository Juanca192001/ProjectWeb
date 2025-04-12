from django.shortcuts import render
from .models import Tipo, Marca, Model

def home(request):
    tipos = Tipo.objects.all()
    marcas = Marca.objects.all()
    modelos = Model.objects.all()
    context = {
        'coches': tipos,
        'marcas': marcas,
        'modelos': modelos
    }
    return render(request, 'ProyectoWeb/home.html',context)

def login_view(request):
    return render(request, 'ProyectoWeb/login.html')
