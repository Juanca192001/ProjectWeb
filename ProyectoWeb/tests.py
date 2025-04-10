from django.test import TestCase

class CocheTestCase(TestCase):
    def test_creacion_coche(self):
        coche = Coche.objects.create(nombre="Test", ruedas="negro", interior="cuero", color="blanco")
        self.assertEqual(coche.nombre, "Test")
        self.assertEqual(coche.ruedas, "negro")
        self.assertEqual(coche.interior, "cuero")
        self.assertEqual(coche.color, "blanco")
