from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
import json

from ProyectoWeb.forms import ConfiguracionForm
from ProyectoWeb.models import Configuracion

times = 0

def login(request):
    global times
    times += 1
    if request.path == '/login/signin/':
        report_loc = '../signin/'
    else:
        report_loc = 'signin/'
    return render(request, 'login.html', {'loc': report_loc, 'error': ''})

def signin(request):
    json2 = open('user_data.json',)
    data = json.load(json2)
    l1 = data['u_data'][0]
    emails = list(l1.keys())
    passwords = list(l1.values())
    json2.close()
    print('Datos leídos desde JSON')
    global times
    times = times + 1
    if request.path == '/login/signin/':
        report_loc = '../signin/'
    else:
        report_loc = 'signin/'
    email = request.POST['email']
    password = request.POST['password']
    if email in emails:
        if passwords[emails.index(email)] == password:
            times = 0
            # Guardar el email en la sesión para indicar que el usuario inició sesión
            request.session['email'] = email
            return redirect('home')
        else:
            return render(request, 'login.html', {
                'loc': report_loc,
                'errorclass': 'alert alert-danger',
                'error': 'Lo sentimos. El email y la contraseña no coinciden.'
            })
    else:
        return render(request, 'login.html', {
            'loc': report_loc,
            'errorclass': 'alert alert-danger',
            'error': 'Lo sentimos. La cuenta no existe. ¡Considere registrarse!'
        })

def register(request):
    global times
    times += 1
    current_url = request.path
    print(current_url)
    print(0)
    if request.path == '/register/signup/':
        report_loc = '../signup/'
    else:
        report_loc = 'signup/'
    return render(request, 'register.html', {'loc': report_loc, 'error': ''})

def signup(request):
    if request.path == '/register/signup/':
        report_loc = '../signup/'
    else:
        report_loc = 'signup/'
    json2 = open('user_data.json',)
    data = json.load(json2)
    l1 = data['u_data'][0]
    emails = list(l1.keys())
    passwords = list(l1.values())
    json2.close()
    email = request.POST['email']
    password = request.POST['password']
    password1 = request.POST['password1']
    usernames = []
    if email not in emails:
        if password == password1:
            emails.append(email)
            passwords.append(password)
            d4 = {emails[len(emails)-1]: passwords[len(emails)-1]}
            for x in range(len(emails)-1):
                d4 = dict(list(d4.items()) + list({emails[x]: passwords[x]}.items()))
            json_object = '{"u_data": [' + json.dumps(d4, indent=4) + ']}'
            a = open('user_data.json', 'w')
            a.write(json_object)
            a.close()
            times = 0
            return redirect('login')
        else:
            return render(request, 'register.html', {
                'loc': report_loc,
                'errorclass': 'alert alert-danger',
                'error': 'Lo sentimos. Las contraseñas no coinciden.'
            })
    else:
        return render(request, 'register.html', {
            'loc': report_loc,
            'errorclass': 'alert alert-danger',
            'error': 'Lo sentimos. El nombre de usuario o el correo ya están en uso.'
        })

def logout(request):
    request.session.flush()
    return redirect('home')

@login_required
def mis_configuraciones(request):
    configuraciones = Configuracion.objects.filter(usuario=request.user)
    return render(request, 'mis_configuraciones.html', {'configuraciones': configuraciones})

@login_required
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

@login_required
def borrar_configuracion(request, pk):
    configuracion = get_object_or_404(Configuracion, pk=pk, usuario=request.user)
    if request.method == 'POST':
        configuracion.delete()
        return redirect('mis_configuraciones')
    return render(request, 'confirmar_borrado.html', {'configuracion': configuracion})