from django.views import View
from django.shortcuts import render
from vehiculos.repositories.pais_fabricacion import PaisRepository

repo = PaisRepository()

class PaisListView(View):
    def get(self, request):
        paises = repo.get_all()
        return render(request, 'vehiculos/create.html', {'paises': paises})
