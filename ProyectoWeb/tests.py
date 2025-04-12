from django.test import TestCase
from .models import Marca, Modelo, Coche

class CocheTestCase(TestCase):
    def setUp(self):
        # Set up data for the tests
        self.marca_seat = Marca.objects.create(nombre="Seat")
        self.modelo_ibiza = Modelo.objects.create(marca=self.marca_seat, nombre="Ibiza")

    def test_creacion_coche(self):
        coche = Coche.objects.create(
            marca=self.marca_seat,
            modelo=self.modelo_ibiza,
            tipo="SUV",
            ruedas="negro",
            interior="cuero",
            color="blanco"
        )
        self.assertEqual(coche.marca, self.marca_seat)
        self.assertEqual(coche.modelo, self.modelo_ibiza)
        self.assertEqual(coche.tipo, "SUV")
        self.assertEqual(coche.ruedas, "negro")
        self.assertEqual(coche.interior, "cuero")
        self.assertEqual(coche.color, "blanco")

    def test_coche_str(self):
        coche = Coche.objects.create(
            marca=self.marca_seat,
            modelo=self.modelo_ibiza,
            tipo="Berlina",
            ruedas="default",
            interior="default",
            color="negro"
        )
        self.assertEqual(str(coche), "Seat Ibiza (Berlina)")
