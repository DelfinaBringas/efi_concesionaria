from django.shortcuts import redirect, render
from vehiculos.models import Pais_fabricacion
from vehiculos.repositories.pais_fabricacion import PaisRepository

repo = PaisRepository()

def pais_list(request):
    pais = repo.get_all()
    return render(
        request,
        'vehiculos/create.html',
        {'paises': pais}
    )