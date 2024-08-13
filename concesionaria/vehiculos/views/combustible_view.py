from django.views import View
from django.shortcuts import render
from vehiculos.repositories.combustible import CombustibleRepository

class CombustibleListView(View):
    def get(self, request):
        repo = CombustibleRepository()
        combustibles = repo.get_all()
        return render(request, 'vehiculos/create.html', {'combustibles': combustibles})
