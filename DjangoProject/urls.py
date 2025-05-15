"""
URL configuration for DjangoProject project.
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from ProyectoWeb.views import (
    home, configuraTuVehiculo, guardar_configuracion, audi_models, volkswagen_models, bmw_models, configurar_model
)
from User import views

from User.views import login, register, logout


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('logout/', logout, name='logout'),
    path('configuraTuVehiculo/', configuraTuVehiculo, name='configuraTuVehiculo'),
    path('configuraTuVehiculo/guardar/', guardar_configuracion, name='guardar_configuracion'),
    path('configuraTuVehiculo/audi/', audi_models, name='audiModels'),
    path('configuraTuVehiculo/<str:marca>/<str:modelo>/', configurar_model, name='configurarModel'),
    path('configuraTuVehiculo/bmw/', bmw_models, name='bmwModels'),
    path('configuraTuVehiculo/volkswagen/', volkswagen_models, name='volkswagenModels'),

]