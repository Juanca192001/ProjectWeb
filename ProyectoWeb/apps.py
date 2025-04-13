from django.apps import AppConfig

from django.apps import AppConfig

INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        # Agrega aquí tu app, por ejemplo:
        'ProyectoWeb',
        'User',
    ]

class ProyectowebConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'ProyectoWeb'

class ProyectowebConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'ProyectoWeb'
