from django.contrib import admin
from .models import Marca, Modelo, Coche

@admin.register(Marca)
class MarcaAdmin(admin.ModelAdmin):
    list_display = ('nombre',)

@admin.register(Modelo)
class ModeloAdmin(admin.ModelAdmin):
    list_display = ('marca', 'nombre')
    list_filter = ('marca',)

@admin.register(Coche)
class CocheAdmin(admin.ModelAdmin):
    list_display = ('marca', 'modelo', 'tipo', 'ruedas', 'interior', 'color')
    list_filter = ('marca', 'modelo', 'tipo')
    search_fields = ('modelo__nombre',)  # Search by model name

