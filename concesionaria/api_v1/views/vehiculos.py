from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework import viewsets
from api_v1.filters import VehiculoFilter
from api_v1.serializer.vehiculo_serializer import VehiculoSerializer
from vehiculos.models import Vehiculo, Comentario, Marca, Modelo, Tipo_combustible, Pais_fabricacion, Color
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAdminUser
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
import csv

class VehiculoViewSet(ModelViewSet):  
    queryset = Vehiculo.objects.all()
    serializer_class = VehiculoSerializer
    filter_backends = [SearchFilter, DjangoFilterBackend]
    search_fields = ['modelo', 'marca']
    filterset_class = VehiculoFilter

    def get_permissions(self):
        if self.action in ['update', 'destroy', 'create']:
            self.permission_classes = [IsAdminUser]
        return super().get_permissions()  

    def create(self, request, *args, **kwargs):
        data = request.data

        required_fields = ['marca', 'modelo', 'precio_dolares', 'tipo_combustible', 'pais_fabricacion', 'color']
        for field in required_fields:
            if field not in data or data[field] is None:
                return Response({ "detail": f"El campo '{field}' es obligatorio." }, status=status.HTTP_400_BAD_REQUEST)

        try:
            precio_dolares = float(data['precio_dolares'])
        except (ValueError, TypeError):
            return Response({ "detail": "El campo 'precio_dolares' debe ser un número decimal." }, status=status.HTTP_400_BAD_REQUEST)

        try:
            marca = Marca.objects.get(id=data['marca'])
            modelo = Modelo.objects.get(id=data['modelo'])
            tipo_combustible = Tipo_combustible.objects.get(id=data['tipo_combustible'])
            pais_fabricacion = Pais_fabricacion.objects.get(id=data['pais_fabricacion'])
            color = Color.objects.get(id=data['color'])
        except ObjectDoesNotExist as e:
            return Response({"detail": f"Error: {str(e)}."}, status=status.HTTP_400_BAD_REQUEST)

        active = data.get('active', 'false') == 'true' 

        # Crear el vehículo
        vehiculo = Vehiculo.objects.create(
            marca=marca,
            modelo=modelo,
            fabricado_el=data.get('fabricado_el'),
            cantidad_puertas=data.get('cantidad_puertas', 4),
            cilindrada=data.get('cilindrada', 0),
            tipo_combustible=tipo_combustible,
            pais_fabricacion=pais_fabricacion,
            precio_dolares=precio_dolares,
            color=color,
            active=active
        )
        serializer = self.get_serializer(vehiculo)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

# delete
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# genera nuevas rutas:
    @action(methods=['get'], detail=False, url_path='download_csv')
    def download_csv(self, request):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="vehiculo.csv"'

        writer = csv.writer(response)
        writer.writerow([
            'marca', 'modelo', 'fabricado_el', 'cantidad_puertas',
            'cilindrada', 'tipo_combustible', 'pais_fabricacion',
            'precio_dolares', 'color'
        ])

        for vehiculo in self.get_queryset():
            writer.writerow([
                vehiculo.marca.nombre if vehiculo.marca else '',
                vehiculo.modelo.nombre if vehiculo.modelo else '',
                vehiculo.fabricado_el,
                vehiculo.cantidad_puertas,
                vehiculo.cilindrada,
                vehiculo.tipo_combustible.nombre if vehiculo.tipo_combustible else '',
                vehiculo.pais_fabricacion.nombre if vehiculo.pais_fabricacion else '',
                vehiculo.precio_dolares,
                vehiculo.color.nombre if vehiculo.color else ''
            ])

        return response
    
    @action(methods=['get'], detail=False, url_path='ultimo_vehiculo')
    def last_vehiculo(self, request):
        last_vehiculo = self.get_queryset().last()
        serializer= self.serializer_class(last_vehiculo)
        return Response(serializer.data)

