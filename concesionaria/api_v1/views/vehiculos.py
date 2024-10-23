from rest_framework.viewsets import ModelViewSet
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser
from api_v1.serializer.vehiculo_serializer import VehiculoSerializer, ComentarioSerializer
from vehiculos.models import Vehiculo, Comentario

class VehiculoViewSet (ModelViewSet):
    queryset = Vehiculo.objects.all()
    serializer_class= VehiculoSerializer


class ComentarioViewSet(viewsets.ModelViewSet):
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer


    # def get_permissions(self):
    #     if self.action in ['update', 'partial_update', 'destroy']:
    #         self.permission_classes = [IsAdminUser]
    #     return super().get_permissions()
