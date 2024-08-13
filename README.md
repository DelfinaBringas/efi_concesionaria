# efi_concesionaria
# Configuración del Proyecto Django:

Clonar el Repositorio:
- git clone git@github.com:DelfinaBringas/efi_concesionaria.git

Obtendras el directorio concesionaria

Fuera del directorio deberas crear tu entorno virtual
- python3 -m venv env

Activar el entorno virtual:
- source env/bin/activate 

Ingresa a concesionaria:
- cd efi_concesionaria

Instalar las dependencias:
- pip install -r requirements.txt

Configurar la Base de Datos: 
- python manage.py makemigrations
- python manage.py migrate

Crear un Superusuario: 
- python manage.py createsuperuser

Ejecutar el servidor:
- python3 manage.py runserver


