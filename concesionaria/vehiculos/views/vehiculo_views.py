from django.shortcuts import render, redirect,get_object_or_404
from vehiculos.repositories.vehiculo import VehiculoRepository
from vehiculos.repositories.marca import MarcaReposository
from vehiculos.repositories.modelo import ModeloReposository
from vehiculos.repositories.combustible import CombustibleRepository
from vehiculos.repositories.pais_fabricacion import PaisRepository

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





