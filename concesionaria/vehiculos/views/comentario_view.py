from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from vehiculos.models import Vehiculo, Comentario
from vehiculos.forms import ComentarioForm
from vehiculos.repositories.comentario import ComentarioRepository
from vehiculos.repositories.vehiculo import VehiculoRepository

@login_required
def comentario_list(request, vehiculo_id):
    vehiculo = get_object_or_404(VehiculoRepository.get_all(), id=vehiculo_id)
    comentarios = ComentarioRepository.get_all().filter(vehiculo=vehiculo)
    return render(
        request,
        'vehiculos/comentarios.html',
        {
            'vehiculo': vehiculo,
            'comentarios': comentarios
        }
    )

@login_required
def comentario_create(request, vehiculo_id):
    vehiculo = get_object_or_404(Vehiculo, id=vehiculo_id)

    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            ComentarioRepository.create(
                vehiculo=vehiculo,
                author=request.user,  
                texto=form.cleaned_data['texto']
            )
            return redirect('comentario_list', vehiculo_id=vehiculo_id)
    else:
        form = ComentarioForm()

    return render(
        request,
        'vehiculos/comentario_create.html',
        {
            'form': form,
            'vehiculo': vehiculo
        }
    )

@login_required
def comentario_update(request, comentario_id):
    comentario = get_object_or_404(Comentario, id=comentario_id)

    if request.method == 'POST':
        form = ComentarioForm(request.POST, instance=comentario)
        if form.is_valid():
            ComentarioRepository.update(
                id=comentario.id,  
                texto=form.cleaned_data['texto']  # Nuevo texto
            )
            return redirect('comentario_list', vehiculo_id=comentario.vehiculo.id)
    else:
        form = ComentarioForm(instance=comentario)

    return render(
        request,
        'vehiculos/comentario_update.html',
        {
            'form': form,
            'comentario': comentario
        }
    )
@login_required
def comentario_delete(request, id):
    comentario = get_object_or_404(Comentario, id=id)
    vehiculo_id = comentario.vehiculo.id 
    if request.method == 'POST':
        ComentarioRepository.delete(comentario)
        return redirect('comentario_list', vehiculo_id=vehiculo_id)
    return redirect('comentario_list', vehiculo_id=vehiculo_id)
