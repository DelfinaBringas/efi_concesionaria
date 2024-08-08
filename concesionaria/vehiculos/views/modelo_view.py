from django.shortcuts import redirect, render

from vehiculos.models import Modelo
from vehiculos.repositories.modelo import ModeloReposository

repo = ModeloReposository()

def modelo_list(request):
    modelos = repo.get_all()
    return render(
        request,
        'vehiculos/create.html',
        {'modelos': modelos}
    )

def index_view(request):
    return render(
        request,
        'index/index.html' )