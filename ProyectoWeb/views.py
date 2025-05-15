from django.shortcuts import render
from .models import Tipo, Marca, Model
from django.http import HttpResponseRedirect
from django.urls import reverse


def home(request):
    tipos = Tipo.objects.all()
    marcas = Marca.objects.all()
    modelos = Model.objects.all()
    context = {
        'coches': tipos,
        'marcas': marcas,
        'modelos': modelos
    }
    return render(request, 'home.html', context)

def configuraTuVehiculo(request):
    tipos = Tipo.objects.all()
    marcas = Marca.objects.all()
    modelos = Model.objects.all()
    context = {
        'coches': tipos,
        'marcas': marcas,
        'modelos': modelos
    }
    return render(request, 'configuraTuVehiculo.html', context)

def guardar_configuracion(request):
    if request.method == 'POST':
        marca = request.POST.get('marca')
        modelo = request.POST.get('modelo')
        color = request.POST.get('color')
        motor = request.POST.get('motor')
        extras = request.POST.getlist('extras')

        # Aquí pots guardar la configuració en la base de dades, sessió, etc.
        print("Configuració rebuda:", marca, modelo, color, motor, extras)

        # Redirigeix a la home o una pàgina de resum
        return HttpResponseRedirect(reverse('home'))

    return HttpResponseRedirect(reverse('configuraTuVehiculo'))

def audi_models(request):
    return render(request, 'audiModels.html')

def volkswagen_models(request):
    return render(request, 'volkswagenModels.html')

def bmw_models(request):
    return render(request, 'bmwModels.html')

def configurar_model(request, marca, modelo):
    return render(request, 'configurarModel.html', {
        'marca': marca,
        'modelo': modelo
    })