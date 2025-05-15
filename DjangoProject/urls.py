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
    home, configuraTuVehiculo,
    audi_config, seat_config, volkswagen_config, guardar_configuracion,
)

from User.views import login, signin, register, signup, logout, mis_configuraciones, editar_configuracion, borrar_configuracion

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('login/', login, name='login'),
    path('login/signin/', signin, name='signin'),
    path('register/', register, name='register'),
    path('register/signup/', signup, name='signup'),
    path('logout/', logout, name='logout'),
    path('configuraTuVehiculo/', configuraTuVehiculo, name='configuraTuVehiculo'),
    path('configuraTuVehiculo/guardar/', guardar_configuracion, name='guardar_configuracion'),
    path('configuraTuVehiculo/audi/', audi_config, name='configura_audi'),
    path('configuraTuVehiculo/seat/', seat_config, name='configura_seat'),
    path('configuraTuVehiculo/volkswagen/', volkswagen_config, name='configura_volkswagen'),
    path('mis-configuraciones/', mis_configuraciones, name='mis_configuraciones'),
    path('editar-configuracion/<int:pk>/', editar_configuracion, name='editar_configuracion'),
    path('borrar-configuracion/<int:pk>/', borrar_configuracion, name='borrar_configuracion'),


]
