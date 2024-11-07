Proyecto Django: Sistema de Gestión de Vehículos y Proveedores

Este proyecto es un sistema de gestión de vehículos y proveedores, implementado utilizando Django, el cual incluye funcionalidad para gestionar vehículos, proveedores, comentarios, y usuarios con diferentes roles (Staff y No-Staff). Además, se proporciona una interfaz para gestionar los comentarios de los vehículos y un sistema de autenticación de usuarios.

FUNCIONALIDADES:
Vehículos:

    Listado de vehículos: Muestra todos los vehículos registrados en la base de datos.
    Detalles de vehículos: Muestra la información detallada de un vehículo.
    Crear, actualizar y eliminar vehículos: Funcionalidades disponibles para el usuario Staff.

Proveedores:

    Listado de proveedores: Muestra los proveedores registrados en el sistema.
    Crear, actualizar y eliminar proveedores: Funcionalidades disponibles para el usuario Staff.

Comentarios:

    Los usuarios pueden comentar sobre los vehículos.
    Los usuarios No-Staff pueden editar y eliminar solo sus propios comentarios.
    Los usuarios Staff pueden eliminar cualquier comentario.

Roles y Permisos:

    Staff Users:
        Acceso completo al panel de administración.
        Puede gestionar vehículos y proveedores.
        Puede ver y eliminar comentarios.
    Non-Staff Users:
        No tiene acceso al panel de administración.
        Puede comentar, editar y eliminar solo sus propios comentarios.

INSTALACION:
1) Clonar el repositorio:
git clone < git@github.com:DelfinaBringas>
cd <cd concesionaria/>

2) Crear un entorno virtual:
python -m venv venv
source venv/bin/activate 

3) Instalar dependencias:
pip install -r requirements.txt

4) Configuración de la base de datos:
python manage.py migrate

5) Cargar datos en la base de datos:
python manage.py load_data vehiculos.csv

6) Crear un superusuario: 
python manage.py createsuperuser

7) Correr el proyecto:
python3 manage.py runserver

8) Aplicar idiomas (en - es)
django-admin compilemessages

DOCUMENTACION: 
1. Vehículos
    Listar vehículos:
        Ruta: /api/v1/vehiculos/
        Método: GET
        Descripción: Devuelve una lista de todos los vehículos.
        Parámetros de búsqueda: modelo, marca
        Respuesta exitosa (200):
        
        {
            "marca": {
                "nombre": "Chevrolet",
                "pk": 7
            },
            "modelo": 12,
            "fabricado_el": 2005,
            "cantidad_puertas": 4,
            "cilindrada": 1.6,
            "tipo_combustible": 4,
            "pais_fabricacion": 7,
            "precio_dolares": "56030.00",
            "color": 5,
            "active": true,
            "comentarios": [
                {
                    "id": 55,
                    "vehiculo": 14,
                    "author": 2,
                    "author_nombre": "Delfina",
                    "texto": "auto grande",
                    "fecha": "2024-10-22T19:06:44.153500Z"
                }
            ]
        },

Crear vehículo:

    Ruta: /api_v1/vehiculos/
    Método: POST
    Descripción: Crea un nuevo vehículo.
    Parámetros requeridos: marca, modelo, precio_dolares, tipo_combustible, pais_fabricacion, color
    Respuesta exitosa (201):

        {
        "marca": {
            "nombre": "Toyota",
            "pk": 1
        },
        "modelo": 1,
        "fabricado_el": 2022,
        "cantidad_puertas": 4,
        "cilindrada": 1500.0,
        "tipo_combustible": 1,
        "pais_fabricacion": 1,
        "precio_dolares": "25000.00",
        "color": 1,
        "active": true,
        "comentarios": []
        }

Actualizar vehículo: 

    Ruta: /api_v1/vehiculos/{id}/
    Método: PUT
    Descripción: Actualiza los detalles de un vehículo.
    Parámetros: Los mismos que al crear, pero puedes omitir los campos que no deseas cambiar.

        {
    "id": 4,
    "marca": "Honda",
    "modelo": "X3",
    "tipo_combustible": "Electric",
    "pais_fabricacion": "Brazil",
    "fabricado_el": 2006,
    "cantidad_puertas": 2,
    "cilindrada": 5.5,
    "precio_dolares": "73608.00",
    "active": true,
    "color": 4
    }
    
Eliminar vehículo:
    Ruta: /api_v1/vehiculos/{id}/
    Método: DELETE
    Descripción: Elimina un vehículo.
    Respuesta exitosa (204): Sin contenido.

Descargar vehículos en CSV:
    Ruta: /api_v1/vehiculos/download_csv/
    Método: GET
    Descripción: Descarga todos los vehículos en formato CSV.

Último vehículo creado:
    Ruta: /api_v1/vehiculos/ultimo_vehiculo/
    Método: GET
    Descripción: Devuelve el último vehículo creado.

2. Comentarios
    Listar comentarios:
        Ruta: /api_v1/comentarios/
        Método: GET
        Descripción: Devuelve una lista de todos los comentarios.
        Respuesta exitosa (200):
    {
      "id": 55,
      "vehiculo_id": 14,
      "vehiculo_marca": "Chevrolet",
      "vehiculo_modelo": "Silverado",
      "author": 2,
      "texto": "auto grande",
      "fecha": "2024-10-22T19:06:44.153500Z"
    },

Crear comentario: 
    Ruta: /api_v1/comentarios/create/{vehiculo_id}/
    Método: POST
    Descripción: Crea un nuevo comentario para un vehículo.
    Parámetros requeridos: texto
    Respuesta exitosa (201):
        {
    "vehiculo": 18,
    "author": 6,
    "texto": "comentario12",
    "fecha": "2024-11-07T14:57:29.999407Z"
        }

Eliminar comentario:

    Ruta: /api_v1/comentarios/{id}/
    Método: DELETE
    Descripción: Elimina un comentario específico.

3. Marcas
    Listar marcas:
        Ruta: /api_v1/marcas/
        Método: GET
        Descripción: Devuelve una lista de todas las marcas disponibles.

         {
      "id": 1,
      "nombre": "Toyota"
    },

    Crear marca:
        Ruta: /api_v1/marcas/
        Método: POST
        Descripción: Crea una nueva marca.
        Parámetros requeridos: nombre
        Respuesta exitosa (201):
    
            {
        "nombre": "Marca X",
        "pk": 1
        }

Actualizar marca:

    Ruta: /api_v1/marcas/{id}/
    Método: PUT
    Descripción: Actualiza una marca existente.

        {
    "id": 16,
    "nombre": "lolo"
    }

Eliminar marca:

    Ruta: /api_v1/marcas/{id}/
    Método: DELETE
    Descripción: Elimina una marca.

4. Usuarios

    Listar usuarios:
        Ruta: /api_v1/usuario/
        Método: GET
        Descripción: Devuelve una lista de todos los usuarios registrados.

        {
      "id": 1,
      "password": "pbkdf2_sha256$720000$Gz6cBYNxy4FcGqsFhIXiOY$deGnFdTCCAXGGP509bkOPMjaGopRR4IMfmeIvS5umd4=",
      "last_login": "2024-11-07T03:17:47.654871Z",
      "is_superuser": true,
      "username": "superusuario",
      "first_name": "",
      "last_name": "",
      "email": "d.bringas@itecriocuarto.org.ar",
      "is_staff": true,
      "is_active": true,
      "date_joined": "2024-08-09T01:02:08.384420Z",
      "groups": [],
      "user_permissions": []
    },

    Crear usuario (Admin solo):
        Ruta: /api_v1/usuario/
        Método: POST
        Descripción: Crea un nuevo usuario. Solo accesible por administradores.

                {
        "id": 10,
        "password": "pbkdf2_sha256$720000$WYR5ciCF20mxbHOVYLCxRx$WW2QeeK9GfbB3OZImUHkhUYg78SSkUUoeIjCsS8Fyd4=",
        "last_login": null,
        "is_superuser": false,
        "username": "tomi",
        "first_name": "ruru",
        "last_name": "ruru",
        "email": "ruru@gmail.com",
        "is_staff": false,
        "is_active": true,
        "date_joined": "2024-11-07T15:18:58.698082Z",
        "groups": [],
        "user_permissions": []
        }



    Eliminar usuario:
        Ruta: /api_v1/usuarios/{id}/
        Método: DELETE
        Descripción: Elimina un usuario.


