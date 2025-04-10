from django.contrib import admin
from .models import Coche

@admin.register(Coche)
class CocheAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'ruedas', 'interior', 'color')
    search_fields = ('nombre',)
