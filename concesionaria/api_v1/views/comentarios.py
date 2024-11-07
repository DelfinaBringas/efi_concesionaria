from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from vehiculos.models import Comentario, Vehiculo
from django.contrib.auth.models import User
from api_v1.serializer.comentarios_serializer import ComentarioSerializer

class ComentariosViewSet(ModelViewSet):
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = super().get_queryset()
        vehiculo_id = self.request.query_params.get('vehiculo')
        if vehiculo_id:
            queryset = queryset.filter(vehiculo_id=vehiculo_id)
        return queryset

    def create(self, request, *args, **kwargs):
        data = request.data

        vehiculo_id = data.get('vehiculo')
        author_id = data.get('author')
        texto = data.get('texto')

        if not vehiculo_id or not author_id or not texto:
            return Response({
                "detail": "vehiculo, author y texto son campos requeridos."
            }, status=status.HTTP_400_BAD_REQUEST)

        try:
            vehiculo = Vehiculo.objects.get(id=vehiculo_id)
        except Vehiculo.DoesNotExist:
            return Response({"detail": "El vehículo con ese ID no existe."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = User.objects.get(id=author_id)
        except User.DoesNotExist:
            return Response({"detail": "El usuario con ese ID no existe."}, status=status.HTTP_400_BAD_REQUEST)

        comentario = Comentario.objects.create(
            vehiculo=vehiculo,
            author=user,
            texto=texto
        )

        serializer = self.serializer_class(comentario)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
