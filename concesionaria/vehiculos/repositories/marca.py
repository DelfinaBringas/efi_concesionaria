from typing import List,Optional
from vehiculos.models import Marca

class MarcaReposository:
    def get_all(self) -> List[Marca]:
        return Marca.objects.all()
    
    def get_by_id(self, id: int) -> Optional[Marca]:
        try:
            return Marca.objects.get(id=id)
        except Marca.DoesNotExist:
            return None

    def create(
        self,
        nombre: str,
    ) -> Marca:
        return Marca.objects.create(
            nombre=nombre,
        )

    def delete(self, marca: Marca):
        return marca.delete()

    def update(
    self,
    marca: Marca,
    nombre: str,
) -> Marca:
        marca.nombre = nombre

        marca.save()
        return marca