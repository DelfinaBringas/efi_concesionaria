from typing import List, Optional
from vehiculos.models import Vehiculo,Marca,Modelo,Tipo_combustible,Color,Pais_fabricacion
#precio
class VehiculoRepository:
    def get_all(self) -> List[Vehiculo]:
        return Vehiculo.objects.all()
    
    def filter_by_id(Self,id:int) -> Optional[Vehiculo]:
        return Vehiculo.objects.filter(id=id).first()

    def get_by_id (self,id:int) -> Optional[Vehiculo]:
        try: 
            vehiculo= Vehiculo.objects.get(id=id)
        except Vehiculo.DoesNotExist:
            vehiculo= None
        return vehiculo
    
    def get_vehiculo_on_price_range(
            self,
            min_price:float,
            max_price:float,
    ) -> List[Vehiculo]:
        vehiculos = Vehiculo.objects.filter(
            precio_dolares__range=(min_price,max_price)
        )
    
    def filter_by_marca(
            self,
            marca=Marca,
    ) -> List[Vehiculo]:
        return Vehiculo.objects.filter(marca=marca)
    
    def delete(Self, vehiculo: Vehiculo):
         vehiculo.delete()

    def create (
        self,
        marca:Marca,
        cilindrada: float,
        cantidad_puertas: int,
        precio_dolares:float,
        fabricado_el: int,
        modelo:Optional[Modelo] = None,
        tipo_combustible: Optional[Tipo_combustible] = None,
        color: Optional[Color] = None,
        pais_fabricacion:Optional[Pais_fabricacion]=None

    ) -> Vehiculo:
        return Vehiculo.objects.create(
            marca=marca,
            cilindrada=cilindrada,
            cantidad_puertas=cantidad_puertas,
            pais_fabricacion=pais_fabricacion,
            precio_dolares=precio_dolares,
            fabricado_el= fabricado_el,
            modelo=modelo,
            tipo_combustible=tipo_combustible,
            color=color,
        )
    
    def update(
        self,
        vehiculo: Vehiculo,
        marca: Marca,
        cilindrada: float,
        cantidad_puertas: int,
        precio_dolares: float,
        fabricado_el: int,
        modelo: Optional[Modelo] = None,
        tipo_combustible: Optional[Tipo_combustible] = None,
        color: Optional[Color] = None,
        pais_fabricacion: Optional[Pais_fabricacion] = None
    ) -> Vehiculo:
        vehiculo.marca = marca
        vehiculo.cilindrada = cilindrada
        vehiculo.cantidad_puertas = cantidad_puertas
        vehiculo.pais_fabricacion = pais_fabricacion
        vehiculo.precio_dolares = precio_dolares
        vehiculo.fabricado_el = fabricado_el
        vehiculo.modelo = modelo
        vehiculo.tipo_combustible = tipo_combustible
        vehiculo.color = color

        vehiculo.save()
        return vehiculo

  
    
