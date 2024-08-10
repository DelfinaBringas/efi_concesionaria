from django.shortcuts import render, redirect,get_object_or_404
from vehiculos.repositories.vehiculo import VehiculoRepository
from vehiculos.repositories.marca import MarcaReposository
from vehiculos.repositories.modelo import ModeloReposository
from vehiculos.repositories.combustible import CombustibleRepository
from vehiculos.repositories.pais_fabricacion import PaisRepository
from vehiculos.repositories.color import ColorRepository
from vehiculos.models import Vehiculo, Comentario
from vehiculos.forms import VehiculoForm

vehiculo_repository = VehiculoRepository()

def vehiculo_list(request):
    vehiculos=vehiculo_repository.get_all()
    return render(
        request,
        'vehiculos/list.html',
        {'vehiculos': vehiculos}
    )

def vehiculo_delete(request, id):
    vehiculo = vehiculo_repository.get_by_id(id)
    vehiculo_repository.delete(vehiculo)
    return redirect('vehiculo_list')

def vehiculo_update(request, id):
    vehiculo = get_object_or_404(Vehiculo, id=id)
    
    if request.method == 'POST':
        form = VehiculoForm(request.POST, instance=vehiculo)
        if form.is_valid():
            vehiculo_repository.update(
                vehiculo=vehiculo,
                marca=form.cleaned_data['marca'],  # Debería ser un solo objeto Marca
                modelo=form.cleaned_data['modelo'],  # Debería ser un solo objeto Modelo
                cantidad_puertas=form.cleaned_data['cantidad_puertas'],
                cilindrada=form.cleaned_data['cilindrada'],
                tipo_combustible=form.cleaned_data['tipo_combustible'],  # Debería ser un solo objeto Combustible
                pais_fabricacion=form.cleaned_data['pais_fabricacion'],  # Debería ser un solo objeto Pais
                precio_dolares=form.cleaned_data['precio_dolares'],
                color=form.cleaned_data['color'],  # Debería ser un solo objeto Color
                fabricado_el=form.cleaned_data['fabricado_el']
            )
            return redirect('vehiculo_list')
    else:
        form = VehiculoForm(instance=vehiculo)
    
    # Crear instancias de los repositorios
    marca_repo = MarcaReposository()
    modelo_repo = ModeloReposository()
    combustible_repo = CombustibleRepository()
    pais_repo = PaisRepository()
    color_repo = ColorRepository()

    # Obtener los datos necesarios
    marcas = marca_repo.get_all()
    modelos = modelo_repo.get_all()
    combustibles = combustible_repo.get_all()
    paises_fabricacion = pais_repo.get_all()
    colores = color_repo.get_all()

    return render(request, 'vehiculos/create.html', {
        'form': form,
        'marcas': marcas,
        'modelos': modelos,
        'combustibles': combustibles,
        'paises': paises_fabricacion,
        'colores': colores
    })
    
def vehiculo_create(request):
    if request.method == 'POST':
        form = VehiculoForm(request.POST)
        if form.is_valid():
            marca_id = form.cleaned_data['marca'].id
            modelo_id = form.cleaned_data['modelo'].id
            combustible_id = form.cleaned_data['tipo_combustible'].id
            pais_id = form.cleaned_data['pais_fabricacion'].id
            color_id = form.cleaned_data['color'].id

            # Crear instancias de los repositorios
            marca_repo = MarcaReposository()
            modelo_repo = ModeloReposository()
            combustible_repo = CombustibleRepository()
            pais_repo = PaisRepository()
            color_repo = ColorRepository()

            # Obtener los datos necesarios
            marca = marca_repo.get_by_id(marca_id)
            modelo = modelo_repo.get_by_id(modelo_id)
            tipo_combustible = combustible_repo.get_by_id(combustible_id)
            pais_fabricacion = pais_repo.get_by_id(pais_id)
            color = color_repo.get_by_id(color_id)

            # Crear el nuevo vehículo
            vehiculo_nuevo = vehiculo_repository.create(
                marca=marca,
                modelo=modelo,
                cantidad_puertas=form.cleaned_data['cantidad_puertas'],
                fabricado_el=form.cleaned_data['fabricado_el'],
                cilindrada=form.cleaned_data['cilindrada'],
                tipo_combustible=tipo_combustible,
                pais_fabricacion=pais_fabricacion,
                precio_dolares=form.cleaned_data['precio_dolares'],
                color=color,
            )
            return redirect('vehiculo_list')
    else:
        form = VehiculoForm()

    # Crear instancias de los repositorios
    marca_repo = MarcaReposository()
    modelo_repo = ModeloReposository()
    combustible_repo = CombustibleRepository()
    pais_repo = PaisRepository()
    color_repo = ColorRepository()

    # Obtener los datos necesarios para los selects
    marcas = marca_repo.get_all()
    modelos = modelo_repo.get_all()
    combustibles = combustible_repo.get_all()
    paises_fabricacion = pais_repo.get_all()
    colores = color_repo.get_all()

    return render(
        request,
        'vehiculos/create.html',
        {
            'form': form,
            'marcas': marcas,
            'modelos': modelos,
            'combustibles': combustibles,
            'paises': paises_fabricacion,
            'colores': colores
        }
    )

# def vehiculo_comentarios(request, id):
#     vehiculo = vehiculo_repository.get_by_id(id)
#     comentarios = vehiculo.comentarios.all()
#     return render(
#         request,
#         'vehiculos/comentarios.html',
#         {
#             'vehiculo': vehiculo,
#             'comentarios': comentarios
#         }
#     )

def index_view(request):
    return render(request, 'index/index.html')

def vehiculo_detail(request, id):
    vehiculo = get_object_or_404(Vehiculo,id=id)
    comentarios = Comentario.objects.filter(vehiculo=vehiculo) 
    return render(
        request,
        'vehiculos/detail.html', 
        {
            'vehiculo': vehiculo,
            'comentarios': comentarios
        }
    )
        









