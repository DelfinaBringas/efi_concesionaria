from typing import List, Optional
from vehiculos.models import Tipo_combustible

class CombustibleRepository:

    def get_all(self) -> List[Tipo_combustible]:
        return Tipo_combustible.objects.all()

    def get_by_id(self, id: int) -> Optional[Tipo_combustible]:
        try:
            return Tipo_combustible.objects.get(id=id)
        except Tipo_combustible.DoesNotExist:
            return None
    
    def create(self, nombre: str) -> Tipo_combustible:
        return Tipo_combustible.objects.create( nombre= nombre,)
    
    def delete(self, tipo_combustible: Tipo_combustible):
        return tipo_combustible.delete()
    
    def update(
            self,
            combustible: Tipo_combustible,
            nombre: str,
    ) -> Tipo_combustible:
        combustible.nombre = nombre

        combustible.save()
        return combustible