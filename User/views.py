from django.shortcuts import render, HttpResponse, redirect
from django.urls import resolve
from django.utils.text import normalize_newlines

from ProyectoWeb.utils.carapi import obtener_modelos_por_marca
import json
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
            print('Nuevo usuario registrado, devolviendo respuesta HTTP')
            return redirect('login')
        else:
            print('Las contraseñas no coinciden, devolviendo respuesta HTTP')
            return render(request, 'register.html', {
                'loc': report_loc,
                'errorclass': 'alert alert-danger',
                'error': 'Lo sentimos. Las contraseñas no coinciden.'
            })
    else:
        print('El nombre de usuario o el correo ya están en uso, devolviendo respuesta HTTP')
        return render(request, 'register.html', {
            'loc': report_loc,
            'errorclass': 'alert alert-danger',
            'error': 'Lo sentimos. El nombre de usuario o el correo ya están en uso.'
        })

def logout(request):
    request.session.flush()
    return redirect('home')

def listar_marcas(request):
    marcas_data = obtener_marcas()
    return render(request,'marcas.html',{'marcas': marcas_data})

def listar_modelos(request):
    modelos_audi = obtener_modelos_por_marca('audi')
    modelos_bmw = obtener_modelos_por_marca('bmw')
    modelos_volkswagen = obtener_modelos_por_marca('volkswagen')
    return None