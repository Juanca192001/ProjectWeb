from django.contrib import admin
from .models import Marca, Model, Tipo, Motor


@admin.register(Marca)
class MarcaAdmin(admin.ModelAdmin):
    list_display = ('nom',)

@admin.register(Tipo)
class ModeloAdmin(admin.ModelAdmin):
    list_display = ('nom',)

@admin.register(Model)
class TipoAdmin(admin.ModelAdmin):
    list_display = ('nom','tipo', 'marca', 'interior', 'motor', 'roda', 'color')
    list_filter = ('nom','tipo','marca',)

@admin.register(Motor)
class MotorAdmin(admin.ModelAdmin):
    list_display = ('energia', 'cilindrada', 'potencia')
    list_filter = ('energia',)

