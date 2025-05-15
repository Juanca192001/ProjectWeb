from django import forms
from .models import Configuracion, Model

class ConfiguracionForm(forms.ModelForm):
    class Meta:
        model = Configuracion
        fields = ['modelo', 'nombre_personalizado']
        widgets = {
            'modelo': forms.Select(attrs={'class': 'form-control'}),
            'nombre_personalizado': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej. Mi SUV Deportivo'
            }),
        }
        labels = {
            'modelo': 'Modelo de coche',
            'nombre_personalizado': 'Nombre personalizado',
        }
