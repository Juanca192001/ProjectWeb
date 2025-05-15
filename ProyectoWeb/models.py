from django.db import models


class Marca(models.Model):
    nom = models.CharField(max_length=100, verbose_name="Nombre de la marca")

    def __str__(self):
        return self.nom


class Tipo(models.Model):
    tipo_id = models.IntegerField(
        primary_key=True,
        verbose_name="Id tipo de coche"
    )

    nom = models.CharField(
        max_length=100,
        verbose_name="Tipo de coche"
    )

    portes = models.IntegerField(
        verbose_name="Portes"
    )

    asientos = models.IntegerField(
        verbose_name="Asientos"
    )

    def __str__(self):
        return self.nom


class Motor(models.Model):

    nombre = models.CharField(
        max_length=50,
        verbose_name="Nombre del motor"
    )

    descripcion = models.CharField(
        max_length=100,
        verbose_name="Descripcion del motor"
    )

    tipo = models.CharField(
        max_length=30,
        verbose_name="Tipo de motor"
    )

    combustible = models.CharField(
        max_length=30,
        verbose_name="Combustible"
    )

    cilindrada = models.CharField(
        max_length=10,
        verbose_name="Cilindrada"
    )

    potencia = models.CharField(
        max_length=10,
        verbose_name="Caballos de potencia"
    )

    def __str__(self):
        return f"{self.nombre}, {self.descripcion}, {self.tipo}"


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
