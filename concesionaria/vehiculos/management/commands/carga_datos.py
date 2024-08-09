import csv
from typing import Any
from django.core.management.base import BaseCommand, CommandParser
from vehiculos.models import Marca, Vehiculo, Modelo, Tipo_combustible, Color, Pais_fabricacion

class Command(BaseCommand):
    help = "Comando encargado de cargar vehículos a partir de un CSV"

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument('archivo_csv', type=str, help="Archivo CSV donde se va a cargar el modelo vehiculo")

    def handle(self, *args, **kwargs) -> str | None:
        self.stdout.write(self.style.WARNING('Iniciando Carga'))
        csv_file = kwargs['archivo_csv']

        with open(csv_file, newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                try:
                    nombre_marca = row['Marca']
                    marca, _ = Marca.objects.get_or_create(nombre=nombre_marca)

                    nombre_modelo = row['Modelo']
                    modelo, _ = Modelo.objects.get_or_create(nombre=nombre_modelo)

                    nombre_tipo_combustible = row['Tipo de Combustible']
                    tipo_combustible, _ = Tipo_combustible.objects.get_or_create(nombre=nombre_tipo_combustible)

                    nombre_color = row['Color']
                    color, _ = Color.objects.get_or_create(nombre=nombre_color)

                    nombre_pais_fabricacion = row['Pais de Fabricacion']
                    pais_fabricacion, _ = Pais_fabricacion.objects.get_or_create(nombre=nombre_pais_fabricacion)

                    vehiculo, created = Vehiculo.objects.get_or_create(
                        marca=marca,
                        modelo=modelo,
                        tipo_combustible=tipo_combustible,
                        color=color,
                        pais_fabricacion=pais_fabricacion,
                        fabricado_el=row['Año de Fabricacion'],
                        cantidad_puertas=row['Cantidad de Puertas'],
                        cilindrada=row['Cilindrada'],
                        precio_dolares=row['Precio en dolares'],
                    )

                    if created:
                        self.stdout.write(self.style.SUCCESS(f'Se cargó el vehículo {vehiculo}'))
                    else:
                        self.stdout.write(self.style.WARNING(f'El vehículo {vehiculo} ya existía'))

                except Marca.DoesNotExist:
                    self.stdout.write(self.style.ERROR(f'Marca no encontrada: {nombre_marca}'))
                except Modelo.DoesNotExist:
                    self.stdout.write(self.style.ERROR(f'Modelo no encontrado: {nombre_modelo}'))
                except Tipo_combustible.DoesNotExist:
                    self.stdout.write(self.style.ERROR(f'Tipo de Combustible no encontrado: {nombre_tipo_combustible}'))
                except Color.DoesNotExist:
                    self.stdout.write(self.style.ERROR(f'Color no encontrado: {nombre_color}'))
                except Pais_fabricacion.DoesNotExist:
                    self.stdout.write(self.style.ERROR(f'País de Fabricación no encontrado: {nombre_pais_fabricacion}'))

        self.stdout.write(self.style.SUCCESS('Finalizada Carga de Vehículos'))
