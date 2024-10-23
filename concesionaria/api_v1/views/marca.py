from rest_framework.viewsets import ModelViewSet
from api_v1.serializer.marca_serializer import MarcaSerializer
from vehiculos.models import Marca


class MarcaViewSet (ModelViewSet):
    queryset = Marca.objects.all()
    serializer_class= MarcaSerializer
    