from django.contrib.auth.models import User
from django.db import models

class Marca(models.Model):
    nom = models.CharField(max_length=100, verbose_name="Nombre de la marca")

    def __str__(self):
        return self.nom

class Tipo(models.Model):
    nom = models.CharField(max_length=100, verbose_name="Tipo de coche")

    def __str__(self):
        return self.nom

class Motor(models.Model):
    ENERGIA_CHOICES = [
        ('gasolina', 'Gasolina'),
        ('diesel', 'Diésel'),
    ]
    energia = models.CharField(
        max_length=20,
        choices=ENERGIA_CHOICES,
        verbose_name="Tipo de energía"
    )

    CILINDRADA_CHOICES = [
        ('1.5', '1.5 L'),
        ('2.0', '2.0 L'),
    ]
    cilindrada = models.CharField(
        max_length=3,
        choices=CILINDRADA_CHOICES,
        verbose_name="Cilindrada"
    )

    POTENCIA_CHOICES = [
        ('100', '100 CV'),
        ('150', '150 CV'),
        ('200', '200 CV'),
    ]
    potencia = models.CharField(
        max_length=3,
        choices=POTENCIA_CHOICES,
        verbose_name="Caballos de potencia"
    )

    def __str__(self):
        return f"{self.energia.capitalize()}, {self.cilindrada}L, {self.potencia}CV"


class Model(models.Model):
    nom = models.CharField(max_length=100, verbose_name="Nombre del modelo")

    tipo = models.ForeignKey(Tipo, on_delete=models.CASCADE, verbose_name="Tipo")

    marca = models.ForeignKey(Marca, on_delete=models.CASCADE, verbose_name="Marca")

    INTERIOR_CHOICES = [
        ('tela', 'Tela'),
        ('cuero', 'Cuero'),
    ]
    interior = models.CharField(
        max_length=10,
        choices=INTERIOR_CHOICES,
        default='tela',
        verbose_name="Interior"
    )

    motor = models.ForeignKey(Motor, on_delete=models.CASCADE, verbose_name="Motor")

    RODA_CHOICES = [
        ('serie', 'Llanta de serie'),
        ('negra', 'Llanta negra'),
    ]
    roda = models.CharField(
        max_length=10,
        choices=RODA_CHOICES,
        verbose_name="Roda (llantas)"
    )

    COLOR_CHOICES = [
        ('#FFFFFF', 'Blanco'),
        ('#000000', 'Negro'),
        ('#808080', 'Gris'),
        ('#FF0000', 'Rojo'),
        ('#0000FF', 'Azul'),
    ]
    color = models.CharField(
        max_length=7,
        choices=COLOR_CHOICES,
        default='#FFFFFF',
        verbose_name="Color (Hexadecimal)"
    )

    def __str__(self):
        return f"{self.marca} {self.nom} ({self.tipo})"

class Configuracion(models.Model):
    usuario = models.ForeignKey(User)
    modelo = models.ForeignKey(Model)
    nombre_personalizado = models.CharField(max_length=100, blank=True, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
