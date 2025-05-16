from django.shortcuts import render, get_object_or_404, redirect

from .forms import ConfiguracionForm,ModelForm
from .models import Tipo, Marca, Model, Configuracion
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


def crear_modelo(request):
    if request.method == 'POST':
        form = ModelForm(request.POST)
        if form.is_valid():
            nuevo_modelo = form.save()
            return redirect('crear_configuracion', modelo_id=nuevo_modelo.id)
    else:
        form = ModelForm()
    return render(request, 'crear_modelo.html', {'form': form})

def crear_modelo(request, marca, modelo):
    # Buscar el objeto Model correspondiente
    marca_obj = get_object_or_404(Marca, nom=marca)
    modelo_obj = get_object_or_404(Model, marca=marca_obj, nom=modelo)

    if request.method == 'POST':
        form = ModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        initial_data = {
            'marca': marca,
            'nom': modelo,
        }
        form = ModelForm(initial=initial_data)

    context = {
        'form': form,
        'marca': marca,
        'modelo': modelo,
        'modelo_id': modelo_obj.id,  # Aquí pasamos el id real
    }
    return render(request, 'configurarModel.html', context)

def guardar_configuracion(request):
    if request.method == 'POST':
        modelo_id = request.POST.get('modelo_id')
        nombre_personalizado = request.POST.get('nombre_personalizado')

        modelo = get_object_or_404(Model, id=modelo_id)

        Configuracion.objects.create(
            usuario=request.user,
            modelo=modelo,
            nombre_personalizado=nombre_personalizado
        )
        # Aquí puedes guardar más campos si tienes en tu modelo Configuracion

        # Después de guardar, redirige a donde quieras
        return redirect('mis_configuraciones')  # o 'home' o la url que prefieras

    # Si no es POST, redirige o muestra un error
    return redirect('home')