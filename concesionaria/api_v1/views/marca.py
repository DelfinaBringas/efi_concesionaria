from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from api_v1.serializer.marca_serializer import MarcaSerializer
from vehiculos.models import Marca
from rest_framework.permissions import IsAdminUser

class MarcaViewSet(ModelViewSet):
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer

    def get_permissions(self):
        if self.action in ['update', 'destroy', 'create']:
            self.permission_classes = [IsAdminUser]
        return super().get_permissions()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            marca = serializer.save()  
            return Response(MarcaSerializer(marca).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, *args, **kwargs):
        instance = self.get_object()  
        serializer = self.get_serializer(instance, data=request.data, partial=True) 

        if serializer.is_valid():
            marca = serializer.save()  
            return Response(MarcaSerializer(marca).data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # delete
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)