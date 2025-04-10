from django.db import models

class Marca(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Modelo(models.Model):
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.marca} - {self.nombre}"

class Coche(models.Model):
    TIPO_CHOICES = [
        ('SUV', 'SUV'),
        ('Berlina', 'Berlina'),
        ('Todo Terreno', 'Todo Terreno'),
    ]
    RUEDAS_CHOICES = [('default', 'Default'), ('negro', 'Negro')]
    INTERIOR_CHOICES = [('default', 'Default'), ('cuero', 'Cuero')]
    COLOR_CHOICES = [('blanco', 'Blanco'), ('negro', 'Negro')]

    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    modelo = models.ForeignKey(Modelo, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)
    ruedas = models.CharField(max_length=10, choices=RUEDAS_CHOICES, default='default')
    interior = models.CharField(max_length=10, choices=INTERIOR_CHOICES, default='default')
    color = models.CharField(max_length=10, choices=COLOR_CHOICES, default='blanco')

    def __str__(self):
        return f"{self.marca} {self.modelo} ({self.tipo})"

