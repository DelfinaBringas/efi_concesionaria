from typing import List, Optional
from vehiculos.models import Proveedor

class ProveedorRepository:
    def get_all(self) ->List[Proveedor]:
        return Proveedor.objects.all()
    
    def get_by_id(self, id:int) -> Optional[Proveedor]:
        return Proveedor.objects.get(id=id)
    
    def delete(self, proveedor:Proveedor):
        proveedor.delete()
    
    def create(
            self,
            nombre:str,
            direccion:str,
            telefono:int,
    ) -> Proveedor:
        proveedor= Proveedor.objects.filter(nombre=nombre)

        return Proveedor.objects.create(
            nombre=nombre,
            direccion=direccion,
            telefono=telefono,
        )
    
    def update(
        self, 
        proveedor: Proveedor,
        nombre:str,
        direccion:str,
        telefono:int,
        ):
          proveedor.nombre=nombre
          proveedor.direccion=direccion
          proveedor.telefono=telefono
          proveedor.save()