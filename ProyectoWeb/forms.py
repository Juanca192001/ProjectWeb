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

class ModelForm(forms.ModelForm):
    class Meta:
        model = Model
        fields = [
            'nom',
            'tipo',
            'marca',
            'interior',
            'motor',
            'roda',
            'color',
        ]
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control'}),
            'tipo': forms.Select(attrs={'class': 'form-control'}),
            'marca': forms.Select(attrs={'class': 'form-control'}),
            'interior': forms.Select(attrs={'class': 'form-control'}),
            'motor': forms.Select(attrs={'class': 'form-control'}),
            'roda': forms.Select(attrs={'class': 'form-control'}),
            'color': forms.Select(attrs={'class': 'form-control'}),
        }