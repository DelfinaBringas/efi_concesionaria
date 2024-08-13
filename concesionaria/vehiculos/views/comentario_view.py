from django.views import View
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from vehiculos.models import Comentario, Vehiculo
from vehiculos.forms import ComentarioForm
from django.http import HttpResponseForbidden

class ComentarioListView(View):
    def get(self, request, vehiculo_id):
        comentarios = Comentario.objects.filter(vehiculo_id=vehiculo_id)
        vehiculo = get_object_or_404(Vehiculo, id=vehiculo_id)
        context = {
            'comentarios': comentarios,
            'vehiculo': vehiculo,
        }
        return render(request, 'comentario/list.html', context)


class ComentarioCreateView(LoginRequiredMixin, View):
    def get(self, request, vehiculo_id):
        vehiculo = get_object_or_404(Vehiculo, id=vehiculo_id)
        form = ComentarioForm()
        return render(request, 'comentario/create.html', {'vehiculo': vehiculo, 'form': form})

    def post(self, request, vehiculo_id):
        vehiculo = get_object_or_404(Vehiculo, id=vehiculo_id)
        form = ComentarioForm(request.POST)
        user = request.user

        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.vehiculo = vehiculo
            comentario.author = user
            comentario.save()
            return redirect('comentario_list', vehiculo_id=vehiculo_id)
        return render(request, 'comentario/create.html', {'vehiculo': vehiculo, 'form': form})

    def post(self, request, vehiculo_id):
        vehiculo = get_object_or_404(Vehiculo, id=vehiculo_id)
        form = ComentarioForm(request.POST)
        user = request.user

        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.vehiculo = vehiculo
            comentario.author = user
            comentario.save()
            return redirect('comentario_list', vehiculo_id=vehiculo_id)
        else:
            print(form.errors) 
            return render(
                request,
                'comentario/create.html',
                {
                    'vehiculo': vehiculo,
                    'form': form
                }
            )

class ComentarioDetailView(View):
    def get(self, request, id):
        comentario = get_object_or_404(Comentario, id=id)
        vehiculo = comentario.vehiculo
        return render(request, 'comentario/detail.html', {'comentario': comentario, 'vehiculo': vehiculo})

class ComentarioUpdateView(LoginRequiredMixin, View):
    login_url = 'login'

    def get(self, request, id):
        comentario = get_object_or_404(Comentario, id=id)
        # Verificar si el usuario es el autor del comentario
        if request.user != comentario.author:
            return HttpResponseForbidden("No tienes permiso para editar este comentario.")
        
        form = ComentarioForm(instance=comentario)
        return render(request, 'comentario/update.html', {'form': form, 'comentario': comentario})

    def post(self, request, id):
        comentario = get_object_or_404(Comentario, id=id)
        # Verificar si el usuario es el autor del comentario
        if request.user != comentario.author:
            return HttpResponseForbidden("No tienes permiso para editar este comentario.")
        
        form = ComentarioForm(request.POST, instance=comentario)
        if form.is_valid():
            form.save()
            return redirect('comentario_detail', id=id)
        return render(request, 'comentario/update.html', {'form': form, 'comentario': comentario})

class ComentarioDeleteView(LoginRequiredMixin, View):
    login_url = 'login'

    def get(self, request, id):
        comentario = get_object_or_404(Comentario, id=id)
        # Verificar si el usuario es el autor del comentario o es staff
        if request.user != comentario.author and not request.user.is_staff:
            return HttpResponseForbidden("No tienes permiso para eliminar este comentario.")
        
        return render(request, 'comentario/confirm_delete.html', {'comentario': comentario})

    def post(self, request, id):
        comentario = get_object_or_404(Comentario, id=id)
        # Verificar si el usuario es el autor del comentario o es staff
        if request.user != comentario.author and not request.user.is_staff:
            return HttpResponseForbidden("No tienes permiso para eliminar este comentario.")
        
        vehiculo_id = comentario.vehiculo.id  # Obtén el vehiculo_id del comentario
        comentario.delete()
        return redirect('comentario_list', vehiculo_id=vehiculo_id)
