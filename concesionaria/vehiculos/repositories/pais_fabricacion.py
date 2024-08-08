from typing import List,Optional
from vehiculos.models import Pais_fabricacion

class PaisRepository:
    def get_all(self) -> List[Pais_fabricacion]:
        return Pais_fabricacion.objects.all()
        
    def get_by_id(self, id: int) -> Optional[Pais_fabricacion]:
        try:
            return Pais_fabricacion.objects.get(id=id)
        except Pais_fabricacion.DoesNotExist:
            return None

    def create(
        self,
        nombre: str,
    ) -> Pais_fabricacion:
        return Pais_fabricacion.objects.create(
            nombre=nombre,
        )
    
    def delete(self, pais: Pais_fabricacion):
        return pais.delete()
    
    def update(
    self,
    pais: Pais_fabricacion,
    nombre: str,
) -> Pais_fabricacion:
        pais.nombre = nombre

        pais.save()
        return pais