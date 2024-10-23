from rest_framework.viewsets import ModelViewSet
from api_v1.serializer.usuario_serializer import UserSerializer
from vehiculos.models import User


class UserViewSet (ModelViewSet):
    queryset = User.objects.all()
    serializer_class= UserSerializer