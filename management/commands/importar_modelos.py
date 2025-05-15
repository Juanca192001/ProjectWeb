from django.core.management.base import BaseCommand
from ProyectoWeb.models import Marca, Model, Motor, Tipo
from ProyectoWeb.utils.carapi import obtener_modelos_por_marca  # Adapta el path si cal

class Command(BaseCommand):
    help = 'Importa models de cotxes des de l’API externa'

    def handle(self, *args, **options):
        marques_api = ['audi', 'bmw', 'volkswagen']

        for marca_slug in marques_api:
            modelos = obtener_modelos_por_marca(marca_slug)

            if not modelos:
                self.stdout.write(self.style.WARNING(f"No s'han trobat models per {marca_slug}"))
                continue

            marca_nom = modelos[0]['marca']
            marca_obj, _ = Marca.objects.get_or_create(nom=marca_nom)

            for modelo in modelos:
                motor_obj, _ = Motor.objects.get_or_create(
                    energia='gasolina',
                    cilindrada='1.5',
                    potencia='100'
                )

                tipo_obj, _ = Tipo.objects.get_or_create(nom='Sedán')

                model_obj, created = Model.objects.get_or_create(
                    nom=modelo['vehiculo'],
                    marca=marca_obj,
                    tipo=tipo_obj,
                    interior='tela',
                    motor=motor_obj,
                    roda='serie',
                    color='#FFFFFF'
                )

                if created:
                    self.stdout.write(self.style.SUCCESS(f"Creat: {model_obj}"))
                else:
                    self.stdout.write(f"Ja existia: {model_obj}")
