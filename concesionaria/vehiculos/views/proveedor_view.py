from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from vehiculos.repositories.proveedor import ProveedorRepository
from vehiculos.models import Proveedor
from vehiculos.forms import ProveedorForm

repo=ProveedorRepository()

def proveedor_list(request):
    proveedor_repository = ProveedorRepository()
    proveedores = proveedor_repository.get_all() 
    return render(
        request,
        'proveedor/list.html',
        {'proveedores': proveedores}  
    )

@login_required
def proveedor_delete(request, id:int):
    repo= ProveedorRepository()
    proveedor= repo.get_by_id(id)
    repo.delete(proveedor)
    return redirect ('proveedor_list')

@login_required
def proveedor_update(request, id):
    proveedor = get_object_or_404(Proveedor, id=id)
    if request.method == 'POST':
        form = ProveedorForm(request.POST, instance=proveedor)
        if form.is_valid():
            form.save()
            return redirect('proveedor_list')
    else:
        form = ProveedorForm(instance=proveedor)

    return render(request, 'proveedor/form.html', {'form': form})

@login_required
def proveedor_create(request):
    if request.method == 'POST':
        form = ProveedorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('proveedor_list')
    else:
        form = ProveedorForm()

    return render(request, 'proveedor/form.html', {'form': form})

@login_required
def proveedor_detail(request, id):
    proveedor = get_object_or_404(Proveedor, id=id)
    
    return render(
        request,
        'proveedor/detail.html',
        {'proveedor': proveedor}
    )
