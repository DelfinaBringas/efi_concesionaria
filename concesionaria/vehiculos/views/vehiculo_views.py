from django.shortcuts import render, redirect,get_object_or_404
from vehiculos.repositories.vehiculo import VehiculoRepository
from vehiculos.repositories.marca import MarcaReposository
from vehiculos.repositories.modelo import ModeloReposository
from vehiculos.repositories.combustible import CombustibleRepository
from vehiculos.repositories.pais_fabricacion import PaisRepository
from vehiculos.forms import VehiculoForm

vehiculo_repository = VehiculoRepository()

def vehiculo_list(request):
    vehiculos=vehiculo_repository.get_all()
    return render(
        request,
        'vehiculos/list.html',
        {'vehiculos': vehiculos}
    )

def vehiculo_delete(request, id):
    vehiculo = vehiculo_repository.get_by_id(id=id)
    vehiculo_repository.delete(vehiculo=vehiculo)
    return redirect('vehiculo_lista')

def vehiculo_update(request, id):
    vehiculo = get_object_or_404(vehiculo_repository.get_all(), id=id)
    if request.method == 'POST':
        form = VehiculoForm(request.POST, instance=vehiculo)
        if form.is_valid(): 
            marca_id = form.cleaned_data['marca'].id
            modelo_id = form.cleaned_data['modelo'].id
            combustible_id = form.cleaned_data['tipo_combustible'].id
            pais_id = form.cleaned_data['pais_fabricacion'].id

            marca = MarcaReposository.get_by_id(marca_id)
            modelo = ModeloReposository.get_by_id(modelo_id)
            tipo_combustible=CombustibleRepository.get_by_id(combustible_id)
            pais_fabricacion=PaisRepository.get_by_id(pais_id)

            vehiculo_nuevo= vehiculo_repository.update(
                vehiculo=vehiculo,
                marca=marca,
                modelo=modelo,
                cantidad_puertas=form.cleaned_data['cantidad_puertas'],
            )







