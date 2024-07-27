# 2024-1-CC4401-2-grupo-1

# Recintos Deportivos

Este es un proyecto Django para gestionar recintos deportivos. La aplicación permite a los usuarios agregar, visualizar y gestionar información sobre diferentes recintos deportivos, incluyendo detalles como nombre, dirección, teléfono, correo electrónico, deportes disponibles, horario y valoración.

## Requisitos Previos

- Python 3.x

## Instalación

1. Clona el repositorio
   - git clone https://github.com/DCC-CC4401/2024-1-CC4401-2-grupo-1.git
   - cd 2024-1-CC4401-2-grupo-1
2. Crea y activa un entorno virtual:
   - python -m venv myvenv
   - myvenv\Scripts\activate
3. Instala las dependencias:
   - pip install -r requirements.txt
4. Realiza las migraciones:
   - python manage.py makemigrations
   - python manage.py migrate
6. Inicia el servidor de desarrollo:
   - python manage.py runserver
7. Accede a la aplicación en tu navegador:
   - http://127.0.0.1:8000.

## Estructura del Proyecto

El proyecto tiene la siguiente estructura:

2024-1-CC4401-2-grupo-1/
- recintos/
- recintosapp/
  - templates/recintosapp
  - static/
    - css/
    - fonts/
    - js/
    - img/
- `manage.py`
- `requirements.txt`


### Archivos Principales

- `recintos/settings.py`: Configuración del proyecto Django.
- `recintos/urls.py`: Definición de las rutas del proyecto.
- `recintosapp/models.py`: Definición de los modelos `User` y `Recinto`.
- `recintosapp/forms.py`: Definición del formulario para el modelo `Recinto`.
- `recintosapp/views.py`: Vistas para manejar la lógica de la aplicación.
- `recintosapp/templates/`: Plantillas HTML para la interfaz de usuario.
- `recintosapp/static/css/`: Estilos CSS para la aplicación.
- `recintosapp/static/js/`: Código JavaScript para la aplicación.
- `recintosapp/static/fonts/`: Fuente personalizada de letra para la vista.
- `recintosapp/static/img/`: Imágenes utilizadas.

## Funcionalidades

- **Página de Inicio**: Muestra un mapa centrado en Santiago con marcadores sobre los recintos deportivos y una tabla de recintos deportivos disponibles. En la esquina superior izquierda tenemos la opcion a hacer login.
- **Autenticación de Usuarios**: Permite a los usuarios registrarse e iniciar sesión.
- **Gestión de Recintos**: Los usuarios admin pueden agregar nuevos recintos deportivos.
- **Comentarios y Valoracion**: Los usuarios registrados pueden comentar y valorar los recintos
- **Filtrado**: Cualquier usuario puede filtrar la tabla de recintos según las preferencias que escoja.