from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from vehiculos.models import Comentario, Vehiculo
from api_v1.serializer.comentarios_serializer import ComentarioSerializer

class ComentariosViewSet(viewsets.ModelViewSet):
    serializer_class = ComentarioSerializer
    permission_classes = [permissions.IsAuthenticated]  

    def get_queryset(self):
        return Comentario.objects.all()

    def vehiculo_comentarios(self, request, pk=None):
        vehiculo_id = pk
        try:
            Vehiculo.objects.get(id=vehiculo_id)
        except Vehiculo.DoesNotExist:
            raise NotFound("Vehículo no encontrado.")

        comentarios = Comentario.objects.filter(vehiculo_id=vehiculo_id)
        serializer = self.get_serializer(comentarios, many=True)
        return Response(serializer.data)
