from django.shortcuts import redirect, render
from vehiculos.models import Tipo_combustible
from vehiculos.repositories.combustible import CombustibleRepository

repo = CombustibleRepository()

def combustible_list(request):
    combustible = repo.get_all()
    return render(
        request,
        'vehiculos/create.html',
        {'combustibles': combustible}
    )
