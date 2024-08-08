from django.shortcuts import redirect, render

from vehiculos.models import Marca
from vehiculos.repositories.marca import MarcaReposository

repo = MarcaReposository()

def marca_list(request):
    marca = repo.get_all()
    return render(
        request,
        'vehiculos/create.html',
        {'marcas': marca}
    )

def index_view(request):
    return render(
        request,
        'index/index.html'  )