from django.views import View
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from vehiculos.repositories.vehiculo import VehiculoRepository
from vehiculos.repositories.marca import MarcaReposository
from vehiculos.repositories.modelo import ModeloReposository
from vehiculos.repositories.combustible import CombustibleRepository
from vehiculos.repositories.pais_fabricacion import PaisRepository
from vehiculos.repositories.color import ColorRepository
from vehiculos.models import Vehiculo, Comentario
from vehiculos.forms import VehiculoForm
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import UserPassesTestMixin

vehiculo_repository = VehiculoRepository()

class VehiculoListView(View):
    def get(self, request):
        vehiculos = vehiculo_repository.get_all()
        return render(request, 'vehiculos/list.html', {'vehiculos': vehiculos})

class VehiculoDeleteView(LoginRequiredMixin, View):
    def post(self, request, id):
        vehiculo = vehiculo_repository.get_by_id(id)
        vehiculo_repository.delete(vehiculo)
        return HttpResponseRedirect(reverse('vehiculo_list'))

class VehiculoCreateView(UserPassesTestMixin, View):
    def test_func(self):
        return self.request.user.is_staff

    def get(self, request):
        form = VehiculoForm()
        marca_repo = MarcaReposository()
        modelo_repo = ModeloReposository()
        combustible_repo = CombustibleRepository()
        pais_repo = PaisRepository()
        color_repo = ColorRepository()

        context = {
            'form': form,
            'marcas': marca_repo.get_all(),
            'modelos': modelo_repo.get_all(),
            'combustibles': combustible_repo.get_all(),
            'paises': pais_repo.get_all(),
            'colores': color_repo.get_all(),
        }
        return render(request, 'vehiculos/create.html', context)

    def post(self, request):
        form = VehiculoForm(request.POST)
        if form.is_valid():
            marca_id = form.cleaned_data['marca'].id
            modelo_id = form.cleaned_data['modelo'].id
            combustible_id = form.cleaned_data['tipo_combustible'].id
            pais_id = form.cleaned_data['pais_fabricacion'].id
            color_id = form.cleaned_data['color'].id

            marca_repo = MarcaReposository()
            modelo_repo = ModeloReposository()
            combustible_repo = CombustibleRepository()
            pais_repo = PaisRepository()
            color_repo = ColorRepository()

            vehiculo_nuevo = vehiculo_repository.create(
                marca=marca_repo.get_by_id(marca_id),
                modelo=modelo_repo.get_by_id(modelo_id),
                cantidad_puertas=form.cleaned_data['cantidad_puertas'],
                fabricado_el=form.cleaned_data['fabricado_el'],
                cilindrada=form.cleaned_data['cilindrada'],
                tipo_combustible=combustible_repo.get_by_id(combustible_id),
                pais_fabricacion=pais_repo.get_by_id(pais_id),
                precio_dolares=form.cleaned_data['precio_dolares'],
                color=color_repo.get_by_id(color_id),
            )
            return HttpResponseRedirect(reverse('vehiculo_list'))
        return self.get(request)


class VehiculoUpdateView(UserPassesTestMixin, View):
    def test_func(self):
        return self.request.user.is_staff

    def get(self, request, id):
        vehiculo = vehiculo_repository.get_by_id(id)
        form = VehiculoForm(instance=vehiculo)
        marca_repo = MarcaReposository()
        modelo_repo = ModeloReposository()
        combustible_repo = CombustibleRepository()
        pais_repo = PaisRepository()
        color_repo = ColorRepository()

        context = {
            'form': form,
            'marcas': marca_repo.get_all(),
            'modelos': modelo_repo.get_all(),
            'combustibles': combustible_repo.get_all(),
            'paises': pais_repo.get_all(),
            'colores': color_repo.get_all(),
        }
        return render(request, 'vehiculos/create.html', context)

    def post(self, request, id):
        vehiculo = vehiculo_repository.get_by_id(id)
        form = VehiculoForm(request.POST, instance=vehiculo)
        if form.is_valid():
            vehiculo_repository.update(
                vehiculo=vehiculo,
                marca=form.cleaned_data['marca'],
                modelo=form.cleaned_data['modelo'],
                cantidad_puertas=form.cleaned_data['cantidad_puertas'],
                cilindrada=form.cleaned_data['cilindrada'],
                tipo_combustible=form.cleaned_data['tipo_combustible'],
                pais_fabricacion=form.cleaned_data['pais_fabricacion'],
                precio_dolares=form.cleaned_data['precio_dolares'],
                color=form.cleaned_data['color'],
                fabricado_el=form.cleaned_data['fabricado_el']
            )
            return HttpResponseRedirect(reverse('vehiculo_list'))
        return self.get(request, id)


class VehiculoDetailView(View):
    def get(self, request, id):
        vehiculo = vehiculo_repository.get_by_id(id)
        comentarios = Comentario.objects.filter(vehiculo=vehiculo)
        return render(request, 'vehiculos/detail.html', {
            'vehiculo': vehiculo,
            'comentarios': comentarios
        })








