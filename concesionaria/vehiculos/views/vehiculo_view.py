from django.views import View
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render,get_object_or_404, redirect
from vehiculos.repositories.vehiculo import VehiculoRepository
from vehiculos.repositories.marca import MarcaReposository
from vehiculos.repositories.modelo import ModeloReposository
from vehiculos.repositories.combustible import CombustibleRepository
from vehiculos.repositories.pais_fabricacion import PaisRepository
from vehiculos.repositories.color import ColorRepository
from vehiculos.models import Vehiculo, Comentario, ImagenAuto
from vehiculos.forms import VehiculoForm, ImagenAutoForm
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.translation import (activate, get_language, gettext_lazy as _, deactivate)
from users.models import Profile
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

vehiculo_repository = VehiculoRepository() 

class VehiculoListView(View):
    def get(self, request):
        # Configurar el idioma del usuario
        lang = 'es'  
        if request.user.is_authenticated:
            try:
                profile = Profile.objects.get(user=request.user)
                lang = profile.language
            except Profile.DoesNotExist:
                pass
            
        activate(lang)

        # Obtener y ordenar los vehículos
        vehiculos = vehiculo_repository.get_all().order_by('id')  # Asegura el orden por un campo único

        # Paginación
        page_number = request.GET.get('page', 1)
        paginator = Paginator(vehiculos, 20)
        try:
            vehiculos_page = paginator.page(page_number)
        except PageNotAnInteger:
            vehiculos_page = paginator.page(1)
        except EmptyPage:
            vehiculos_page = paginator.page(paginator.num_pages)

        return render(request, 'vehiculos/list.html', {'vehiculos': vehiculos_page})

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
        image_form = ImagenAutoForm()
        context = {
            'form': form,
            'image_form': image_form,
            'marcas': MarcaReposository().get_all(),
            'modelos': ModeloReposository().get_all(),
            'combustibles': CombustibleRepository().get_all(),
            'paises': PaisRepository().get_all(),
            'colores': ColorRepository().get_all(),
        }
        return render(request, 'vehiculos/create.html', context)

    def post(self, request):
        form = VehiculoForm(request.POST)
        image_form = ImagenAutoForm(request.POST, request.FILES)
        
        if form.is_valid() and image_form.is_valid():
            vehiculo_nuevo = vehiculo_repository.create(
                marca=form.cleaned_data['marca'],
                modelo=form.cleaned_data['modelo'],
                cantidad_puertas=form.cleaned_data['cantidad_puertas'],
                fabricado_el=form.cleaned_data['fabricado_el'],
                cilindrada=form.cleaned_data['cilindrada'],
                tipo_combustible=form.cleaned_data['tipo_combustible'],
                pais_fabricacion=form.cleaned_data['pais_fabricacion'],
                precio_dolares=form.cleaned_data['precio_dolares'],
                color=form.cleaned_data['color'],
            )
            
            # Procesar las imágenes subidas
            if 'image' in request.FILES:
                ImagenAuto.objects.create(
                    vehiculo=vehiculo_nuevo,
                    image=request.FILES['image'],
                    description=image_form.cleaned_data.get('description', '')
                )

            return HttpResponseRedirect(reverse('vehiculo_list'))
        
        context = {
            'form': form,
            'image_form': image_form,
            'marcas': MarcaReposository().get_all(),
            'modelos': ModeloReposository().get_all(),
            'combustibles': CombustibleRepository().get_all(),
            'paises': PaisRepository().get_all(),
            'colores': ColorRepository().get_all(),
        }
        return render(request, 'vehiculos/create.html', context)


class VehiculoUpdateView(LoginRequiredMixin, UserPassesTestMixin, View):
    def test_func(self):
        vehiculo = self.get_object()
        return self.request.user.is_staff or vehiculo.creador == self.request.user

    def get_object(self):
        return get_object_or_404(Vehiculo, id=self.kwargs['id'])

    def get(self, request, id):
        vehiculo = self.get_object()
        form = VehiculoForm(instance=vehiculo)
        image_form = ImagenAutoForm()
        context = {
            'form': form,
            'image_form': image_form,
            'marcas': MarcaReposository().get_all(),
            'modelos': ModeloReposository().get_all(),
            'combustibles': CombustibleRepository().get_all(),
            'paises': PaisRepository().get_all(),
            'colores': ColorRepository().get_all(),
        }
        return render(request, 'vehiculos/update.html', context)

    def post(self, request, id):
        vehiculo = self.get_object()
        form = VehiculoForm(request.POST, instance=vehiculo)
        image_form = ImagenAutoForm(request.POST, request.FILES)
        
        if form.is_valid() and image_form.is_valid():
            vehiculo_actualizado = form.save()
            
            # Procesar la carga de nuevas imágenes
            if 'image' in request.FILES:
                ImagenAuto.objects.create(
                    vehiculo=vehiculo_actualizado,
                    image=request.FILES['image'],
                    description=image_form.cleaned_data.get('description', '')
                )

            return HttpResponseRedirect(reverse('vehiculo_list'))
        
        context = {
            'form': form,
            'image_form': image_form,
            'marcas': MarcaReposository().get_all(),
            'modelos': ModeloReposository().get_all(),
            'combustibles': CombustibleRepository().get_all(),
            'paises': PaisRepository().get_all(),
            'colores': ColorRepository().get_all(),
        }
        return render(request, 'vehiculos/update.html', context)

class VehiculoDetailView(View):
    def get(self, request, id):
        vehiculo = vehiculo_repository.get_by_id(id)
        comentarios = Comentario.objects.filter(vehiculo=vehiculo)
        return render(request, 'vehiculos/detail.html', {
            'vehiculo': vehiculo,
            'comentarios': comentarios
        })

class ImagenDeleteView(LoginRequiredMixin, UserPassesTestMixin, View):
    def test_func(self):
        return self.request.user.is_staff

    def post(self, request, imagen_id):
        imagen = get_object_or_404(ImagenAuto, id=imagen_id)
        vehiculo_id = imagen.vehiculo.id  
        imagen.delete()
        return redirect('vehiculo_detail', id=vehiculo_id)  






