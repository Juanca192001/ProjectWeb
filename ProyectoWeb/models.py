from django.db import models

class Coche(models.Model):
    RUEDAS_CHOICES = [('default', 'Default'), ('negro', 'Negro')]
    INTERIOR_CHOICES = [('default', 'Default'), ('cuero', 'Cuero')]
    COLOR_CHOICES = [('blanco', 'Blanco'), ('negro', 'Negro')]

    nombre = models.CharField(max_length=100)
    ruedas = models.CharField(max_length=10, choices=RUEDAS_CHOICES, default='default')
    interior = models.CharField(max_length=10, choices=INTERIOR_CHOICES, default='default')
    color = models.CharField(max_length=10, choices=COLOR_CHOICES, default='blanco')

    def __str__(self):
        return self.nombre
