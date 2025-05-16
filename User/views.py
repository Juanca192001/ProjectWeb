from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from ProyectoWeb.forms import ConfiguracionForm
from ProyectoWeb.models import Configuracion

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Buscar usuario por email
        try:
            user_obj = User.objects.get(email=email)
        except User.DoesNotExist:
            return render(request, 'login.html', {
                'errorclass': 'alert alert-danger',
                'error': 'Este usuario no existe.'
            })

        # Autenticar por username (porque `authenticate` usa username, no email)
        user = authenticate(request, username=user_obj.username, password=password)

        if user is not None:
            auth_login(request, user)  # 🔐 Login automático
            return redirect('home')
        else:
            return render(request, 'login.html', {
                'errorclass': 'alert alert-danger',
                'error': 'La contraseña es incorrecta.'
            })

    return render(request, 'login.html', {'error': ''})
def register(request):
    print('Página de registro abierta')
    if request.method == 'POST':
        username = request.POST.get('name')  # ← Asegúrate de que coincide con el "name" del input
        email = request.POST.get('email')
        password = request.POST.get('password')
        password1 = request.POST.get('password1')

        if password != password1:
            return render(request, 'register.html', {
                'errorclass': 'alert alert-danger',
                'error': 'Lo sentimos. Las contraseñas no coinciden.'
            })

        if User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists():
            return render(request, 'register.html', {
                'errorclass': 'alert alert-danger',
                'error': 'El nombre de usuario o el correo ya están en uso.'
            })

        User.objects.create(
            username=username,
            email=email,
            password=make_password(password)
        )
        return redirect('login')

    return render(request, 'register.html', {'error': ''})

def logout(request):
    auth_logout(request)
    return redirect('home')

def mis_configuraciones(request):
    configuraciones = Configuracion.objects.filter(usuario=request.user)
    return render(request, 'mis_configuraciones.html', {'configuraciones': configuraciones})

def editar_configuracion(request, pk):
    configuracion = get_object_or_404(Configuracion, pk=pk, usuario=request.user)
    if request.method == 'POST':
        form = ConfiguracionForm(request.POST, instance=configuracion)
        if form.is_valid():
            form.save()
            return redirect('mis_configuraciones')
    else:
        form = ConfiguracionForm(instance=configuracion)
    return render(request, 'editar_configuracion.html', {'form': form})

def borrar_configuracion(request, pk):
    configuracion = get_object_or_404(Configuracion, pk=pk, usuario=request.user)
    if request.method == 'POST':
        configuracion.delete()
        return redirect('mis_configuraciones')
    return render(request, 'confirmar_borrado.html', {'configuracion': configuracion})