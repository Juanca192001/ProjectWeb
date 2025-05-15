# GestorProyectos/utils/carapi.py

import requests
from django.conf import settings
from django.shortcuts import render


def obtener_jwt():
    url = "https://carapi.app/api/auth/login"
    headers = {"accept": "text/plain", "Content-Type": "application/json"}
    data = {
        "api_token": settings.CARAPI_TOKEN,
        "api_secret": settings.CARAPI_SECRET
    }
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        return response.text
    return None


def obtener_modelos_por_marca(marca):
    jwt = obtener_jwt()
    url = "https://carapi.app/api/models?verbose=yes&year=2015&make=" + marca + ""
    headers = {"Authorization": f"Bearer {jwt}", "accept": "application/json"}
    response = requests.get(url, headers=headers)
    data = response.json()
    modelo_list = []
    if data:
        for modelo_data in data['data']:
            modelo = {
                'marca': modelo_data['make']['name'],
                'vehiculo': modelo_data['name'],
            }
            modelo_list.append(modelo)
    return modelo_list


def obtener_motores(modelo, marca):
    jwt = obtener_jwt()
    url = "https://carapi.app/api/engines?verbose=yes&year=2015&make=" + marca + "&model=" + modelo + ""
    headers = {"Authorization": f"Bearer {jwt}", "accept": "application/json"}
    response = requests.get(url, headers=headers)
    data = response.json()
    motor_list = []
    if data:
        for motor_data in data['data']:
            motor = {
                'tipus': motor_data['engine_type'],
                'combustible': motor_data['fuel_type'],
                'cilindrada': motor_data['cylinders'],
                'potencia': motor_data['horsepower_hp'],
                'name': motor_data['make_model_trim']['name'],
                'descripció': motor_data['make_model_trim']['description'],
            }
            motor_list.append(motor)
    return motor_list


def obtener_tipos(marca):
    jwt = obtener_jwt()
    url = "https://carapi.app/api/bodies?year=2015&make="+marca
    headers = {"Authorization": f"Bearer {jwt}", "accept": "application/json"}
    response = requests.get(url, headers=headers)
    data = response.json()
    tipos_list = []
    if data:
        for tipo_data in data['data']:
            tipo = {
                'tipo_id': tipo_data['id'],
                'nom': tipo_data['type'],
                'portes': tipo_data['doors'],
                'asientos': tipo_data['seats'],
                'largada': tipo_data['length'],
                'alto': tipo_data['height'],
                'ancho': tipo_data['width'],
                'capacidad': tipo_data['cargo_capacity'],
            }
            tipos_list.append(tipo)
    return tipos_list
