from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from vehiculos.repositories.comentario import ComentarioRepository
from vehiculos.models import Comentario, Vehiculo
from vehiculos.forms import ComentarioForm

# Lista de comentarios
def comentario_list(request):
    comentario_repository = ComentarioRepository()
    comentarios = comentario_repository.get_all() 
    vehiculo = Vehiculo.objects.first() 
    
    # Combina los dos diccionarios en uno solo
    context = {
        'comentarios': comentarios,  # Corregir el nombre de la clave de 'cometarios' a 'comentarios'
        'vehiculo': vehiculo,
    }
    
    return render(request, 'comentario/list.html', context)

# Crear un comentario
@login_required
def comentario_create(request):
    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('comentario_list')  # O redirige a la vista adecuada
    else:
        form = ComentarioForm()
    return render(request, 'comentario/create.html', {'form': form})

# Detalle de un comentario
def comentario_detail(request, id):
    comentario = get_object_or_404(Comentario, id=id)
    return render(request, 'comentario/detail.html', {'comentario': comentario})

# Actualizar un comentario
@login_required
def comentario_update(request, id):
    comentario = get_object_or_404(Comentario, id=id)

    if request.method == 'POST':
        form = ComentarioForm(request.POST, instance=comentario)
        if form.is_valid():
            form.save()
            return redirect('comentario_detail', id=id)
    else:
        form = ComentarioForm(instance=comentario)

    return render(request, 'comentario/update.html', {'form': form, 'comentario': comentario})

# Eliminar un comentario
@login_required
def comentario_delete(request, id):
    comentario = get_object_or_404(Comentario, id=id)

    if request.method == 'POST':
        comentario.delete()
        return redirect('comentario_list')

    return render(request, 'comentario/confirm_delete.html', {'comentario': comentario})
