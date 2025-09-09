# IS-2016-1-LAB
Repositorio de Laboratorio de Ingeniería de Software. Aqui Tendran notas, guias y ejemplos de los laboratorios.

# Clase 1 - 25/08/2016

## Antes de empezar

### ¿Qué es Django?
Es un framework de desarrollo web de código abierto, escrito en Python, que sigue el patrón de diseño Modelo-Vista-Template (MVT).

#### Ventajas
- facilidad de uso
- permite crear algo desde 0 a algo usable en poco tiempo (MVP,Minimum Viable Product)

#### Algunos Ejemplos
almenos en sus primeras versiones:

- Instagram
- Spotify

Para empezar debemos entender que so los entornos virtuales y como instalarlos. Ya que nos ayudan a tener paquetes con versiones especificas para cada proyecto.

## Entornos Virtuales
### ¿Qué es un entorno virtual en Python y por qué usarlo en Django?
Un entorno virtual en Python es un espacio aislado donde puedes instalar paquetes y librerías sin afectar el sistema global. Es especialmente útil cuando trabajas en diferentes proyectos, ya que cada uno puede requerir distintas versiones de las mismas dependencias.

#### ¿Por qué usar entornos virtuales en Django?
Cuando trabajas con Django, podrías tener múltiples proyectos en tu computadora. Algunos podrían usar Django 3.x, mientras que otros requieren Django 4.x. Si instalas Django globalmente, podrías enfrentar conflictos de versiones.

##### Ventajas de usar un entorno virtual: 

- Evita conflictos de versiones entre proyectos.
- Permite probar diferentes versiones de Django sin afectar otros proyectos.
- Mantiene el sistema limpio sin instalar paquetes globalmente.
- Hace que el proyecto sea más portátil y fácil de compartir con otros desarrolladores.

Para crear un entorno virtual en python se utiliza el siguiente comando:

```bash
python -m venv path/nombre_del_entorno
```
### buenas practicas
- crear un archivo `.gitignore` para ignorar los archivos de entorno virtual
- crear un archivo `requirements.txt` para guardar las dependencias del proyecto
- el nombre del entorno virtual debe ser `.venv`
- el entorno virtual debe estar en la carpeta raiz del proyecto

### Activar entorno virtual
En Mac y Linux
```bash
source .venv/bin/activate
```
En Windows
```bash
.venv\Scripts\activate
```
Una vez activado el entorno virtual, el nombre del entorno virtual aparecerá en la terminal.

```bash
(env) usuario@mi-computadora:~/mi_proyecto$
```

### desactivar entorno virtual
En Mac, Linux y Windows
```bash
deactivate
```

Ya teniendo el entorno virtual activado, podemos instalar las dependencias del proyecto (una de esas es Django).


## Instalación de Django

Una vez que tenemos el entorno virtual activado, podemos instalar Django en su ultima version con el siguiente comando:

```bash
pip install django
```

Si queremos instalar una version especifica de Django, podemos hacerlo con el siguiente comando:

```bash
pip install django==x.y.z
```
Siendo x.y.z la version que queremos instalar.

Para verificar la instalacion de django usamos el comando.

```bash
django-admin --version
```
Para cualquier duda sobre los comandos de Django, podemos utilizar el siguiente comando:

```bash
django-admin --help
```


## Git y GitHub
### ¿Qué es Git?
Git es un sistema de control de versiones distribuido que permite a los desarrolladores rastrear cambios
en su código fuente a lo largo del tiempo. Fue creado por Linus Torvalds en 2005 para ayudar en el desarrollo del kernel de Linux.

### ¿Qué es GitHub?
GitHub es una plataforma de alojamiento de código fuente que utiliza Git como sistema de control de versiones. Permite a los desarrolladores colaborar en proyectos, compartir código y gestionar versiones de manera eficiente.

### Por qué usar Git y GitHub en proyectos de Django?
- **Control de versiones**: Permite rastrear cambios en el código, revertir a versiones anteriores y colaborar con otros desarrolladores.
- **Colaboración**: Facilita el trabajo en equipo, permitiendo a múltiples desarrolladores trabajar en el mismo proyecto sin conflictos.
- **Copia de seguridad**: Almacena el código en la nube, proporcionando una copia de seguridad en caso de pérdida de datos.
- **Integración continua**: Permite la integración con herramientas de CI/CD para automatizar pruebas y despliegues.
- **Documentación**: Facilita la documentación del proyecto a través de archivos README y wikis.

### Que es .gitignore
El archivo `.gitignore` es un archivo de texto que le dice a Git qué archivos o carpetas deben ser ignorados en un repositorio. Esto es útil para evitar que archivos temporales, de configuración o de entorno se incluyan en el control de versiones.

### Ejemplo de un archivo .gitignore para un proyecto Django
```
# Ignorar archivos de entorno virtual
.venv/

# Ignorar compilados de Python
__pycache__/
*.pyc
*.pyo
*.pyd
*.sqlite3
```

### Comandos básicos de Git
- `git init`: Inicializa un nuevo repositorio Git en el directorio actual.
- `git clone <url>`: Clona un repositorio remoto en tu máquina local.
- `git add <archivo>`: Añade un archivo al área de preparación (staging area).
- `git commit -m "mensaje"`: Crea un commit con los cambios añadidos al área de preparación.
- `git push`: Sube los commits locales al repositorio remoto.
- `git pull`: Descarga y fusiona cambios desde el repositorio remoto al local.
- `git status`: Muestra el estado actual del repositorio, incluyendo archivos modificados y no rastreados.
- `git log`: Muestra el historial de commits del repositorio.   
- `git branch`: Lista, crea o elimina ramas en el repositorio.
- `git checkout <rama>`: Cambia a la rama especificada.
- `git merge <rama>`: Fusiona la rama especificada en la rama actual.
- `git remote add <name> <url>`: Añade un repositorio remoto con el nombre name.
- `git remote -v`: Muestra los repositorios remotos configurados.
- `git fetch`: Descarga cambios desde el repositorio remoto sin fusionarlos.
- `git reset --hard <commit>`: Restaura el repositorio al estado del commit especificado, descartando todos los cambios posteriores.

### Buenas prácticas al hacer commits
- Hacer commits pequeños y frecuentes.
- Escribir mensajes de commit claros y descriptivos. 
- Usar el tiempo presente en los mensajes de commit.
- Evitar incluir archivos innecesarios en los commits (usar .gitignore).
- Revisar los cambios antes de hacer un commit (usar `git status` y `git diff`).

### Convenciones para mensajes de commit
- Al inicio deberemos colocar un prefijo que indique el tipo de cambio realizado. Algunos ejemplos comunes son:
  - `feat`: para nuevas funcionalidades.
  - `fix`: para correcciones de errores.
  - `docs`: para cambios en la documentación.
  - `style`: para cambios en el formato del código (espacios, tabulaciones, etc.) sin afectar la lógica.
  - `refactor`: para cambios en el código que no añaden funcionalidades ni corrigen errores, pero mejoran la estructura o legibilidad.
  - `test`: para añadir o modificar pruebas.
  - `chore`: para tareas de mantenimiento que no afectan el código fuente ni los tests.
- Después del prefijo, se debe colocar una breve descripción del cambio realizado, separada por dos puntos y un espacio.
- La descripción debe ser concisa pero informativa, idealmente en 50 caracteres o menos

### GitHub Flow
GitHub Flow es un flujo de trabajo simple y efectivo para colaborar en proyectos utilizando Git y GitHub. Se basa en ramas y pull requests para facilitar la colaboración y revisión de código.
#### Pasos de GitHub Flow
1. **Crear una rama**: Cada nueva característica o corrección de error debe desarrollarse en una rama separada. Esto permite trabajar de manera aislada sin afectar la rama principal (main).
    ```bash
    git checkout -b nombre-de-la-rama
    ```
2. **Hacer commits**: Realiza commits pequeños y frecuentes en la rama creada, siguiendo las buenas prácticas mencionadas anteriormente.
    ```bash
    git add .
    git commit -m "feat: añadir nueva funcionalidad"
    ```
3. **Push a la rama**: Sube los cambios de la rama al repositorio remoto en GitHub.
    ```bash
    git push origin nombre-de-la-rama
    ```
4. **Crear un pull request**: Una vez que la funcionalidad o corrección está lista, crea un pull request en GitHub para solicitar la revisión y fusión de los cambios en la rama principal.
5. **Revisión de código**: Otros miembros del equipo revisan el código, hacen comentarios y sugieren mejoras.
6. **Fusión (merge)**: Después de la revisión y aprobación, fusiona la rama en la rama principal esto ya lo hace el pull request.
7. **Eliminar la rama**: Una vez fusionada, elimina la rama para mantener el repositorio limpio esto ya lo hace el pull request.

# Clase 2 - 01/09/2016

## Crear un proyecto en Django

Para crear un proyecto en Django se utiliza el siguiente comando:

```bash
django-admin startproject <nombre_del_proyecto>
```

El nombre del proyecto no debe tener espacios ni `-` si se quiere un nombre compuesto, se puede utilizar guion bajo `_`.

### Estructura de un proyecto en Django

La estructuras del proyecto es la siguiente.

```bash
mi_proyecto/
│── manage.py
│── mi_proyecto/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   ├── wsgi.py
```

- `manage.py`: es un script que ayuda con la administración del proyecto. Con él se pueden crear aplicaciones, crear un servidor de desarrollo, entre otras cosas.
- `nombre_del_proyecto/`: es la carpeta que contiene el proyecto.
  - `__init__.py`: es un archivo que indica que la carpeta es un paquete de Python.
  - `settings.py`: es el archivo de configuración del proyecto. `-Importante`
  - `urls.py`: es el archivo que contiene las urls del proyecto. `-Importante`
  - `wsgi.py`: es el archivo que contiene la configuración para desplegar el proyecto en producción.
  - `asgi.py`: es el archivo que contiene la configuración para desplegar el proyecto en producción con ASGI.

## Correr el servidor

Para correr el servidor de desarrollo de Django se utiliza el siguiente comando (debe estar en la carpeta del proyecto a la altura de `manage.py`):

```bash
python manage.py runserver
```
si tienes dudas sobre los comandos de `manage.py` puedes utilizar el siguiente comando:

```bash
python manage.py --help
```

## Entendiendo la arquitectura MVT

- Modelo: es la representación de los datos que maneja el proyecto.
- Vista: es la logica de datos que maneja el proyecto.
- Template: es la representación visual de los datos que maneja el proyecto.

## Crear una aplicación en Django
A la altura de `manage.py` se utiliza el siguiente comando para crear una aplicación en Django:

```bash
python manage.py startapp <nombre_de_la_aplicacion>
```

### Estructura de una aplicación en Django

- `migrations/`: es la carpeta que contiene las migraciones de la aplicación.
- `__init__.py`: es un archivo que indica que la carpeta es un paquete de Python.
- `admin.py`: es el archivo de configuración del administrador de Django.
- `apps.py`: es el archivo de configuración de la aplicación.
- `models.py`: es el archivo que contiene los modelos de la aplicación.
- `tests.py`: es el archivo que contiene las pruebas de la aplicación.
- `views.py`: es el archivo que contiene las vistas de la aplicación.

### trabajar con la aplicacion en Django

Para trabajar con la aplicación en Django, debemos agregarla en el archivo `settings.py` en la variable `INSTALLED_APPS`.

```python  
INSTALLED_APPS = [
    ...
    'nombre_de_la_aplicacion',
    ...
]
```

## Crear una vista en Django
Para crear una vista en Django, debemos agregar una función en el archivo `views.py` de la aplicación.

```python
from django.http import HttpResponse

def mi_vista(request):
    return HttpResponse("¡Hola, mundo!")
```
Luego, debemos agregar la vista en el archivo `urls.py` del proyecto.

```python
from django.contrib import admin
from django.urls import path
from nombre_de_la_aplicacion.views import mi_vista
urlpatterns = [
    path('admin/', admin.site.urls),
    path('mi_vista/', mi_vista),
]
```

Luego, podemos acceder a la vista en el navegador con la siguiente URL:

http://localhost:8000/mi_vista/

En general no es bueno tener todas las urls en el archivo `urls.py` del proyecto, por lo que es mejor crear un archivo `urls.py` en la aplicación y agregar las urls de la aplicación en ese archivo.

```python
from django.urls import path
from .views import mi_vista

urlpatterns = [
    path('mi_vista/', mi_vista),
]
```
Luego, debemos agregar las urls de la aplicación en el archivo `urls.py` del proyecto.

```python
from django.contrib import admin
from django.urls import path, include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('nombre_de_la_aplicacion/', include('nombre_de_la_aplicacion.urls')),
]
``` 
De esta manera, podemos tener las urls de la aplicación en un solo archivo y no en el archivo del proyecto.

Ojo el url `nombre_de_la_aplicacion/` es opcional, si no se quiere tener ese prefijo en las urls de la aplicación, se puede dejar vacío.

```python
from django.contrib import admin
from django.urls import path, include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('nombre_de_la_aplicacion.urls')),
]
```
De esta manera, podemos acceder a la vista en el navegador con la siguiente URL:

http://localhost:8000/mi_vista/

Como teniamos antes.

## Crear un template en Django
Para crear un template en Django, debemos crear una carpeta llamada `templates` en la carpeta del proyecto y dentro de esa carpeta crear un archivo HTML.
```html
<!-- templates/mi_template.html -->
<!DOCTYPE html>
<html lang="es">
<head><meta charset="UTF-8"></head>
<body>
<h1>¡Hola, mundo!</h1>
</body>
</html>     
```
Luego, debemos configurar la carpeta de templates en el archivo `settings.py` del proyecto.

```python

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```
Luego, debemos modificar la vista para que renderice el template.

```python
from django.shortcuts import render

def mi_vista(request):
    return render(request, 'mi_template.html')
```

Luego, podemos acceder a la vista en el navegador con la siguiente URL:

http://localhost:8000/mi_vista/

## Extender templates en Django
Para extender un template en Django, debemos crear un archivo base en la carpeta `templates`.

```html
<!-- templates/base.html -->
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>{% block title %}Mi sitio web{% endblock %}</title>
</head>
<body>
    <header>
        <h1>Mi sitio web</h1>
        <nav>
            <ul>
                <li><a href="/">Inicio</a></li>
                <li><a href="/about/">Acerca de</a></li>
                <li><a href="/contact/">Contacto</a></li>
            </ul>
        </nav>
    </header>
    <main>
        {% block content %}{% endblock %}
    </main>
    <footer>
        <p>&copy; 2024 Mi sitio web</p>
    </footer>
</body>
</html>
```
Luego, debemos modificar el template para que extienda el template base.

```html
<!-- templates/mi_template.html -->
{% extends 'base.html' %}

{% block title %}Mi template{% endblock %}

{% block content %}
<h1>¡Hola, mundo!</h1>
{% endblock %}
```

Luego, podemos acceder a la vista en el navegador con la siguiente URL:

http://localhost:8000/mi_vista/

## Clase TemplateView
Django proporciona una vista genérica llamada `TemplateView` que facilita la renderización de templates sin necesidad de definir una función de vista personalizada. Esta vista es útil para páginas estáticas o cuando solo necesitas mostrar un template sin lógica adicional.

```python
from django.views.generic import TemplateView

class MiTemplateView(TemplateView):
    template_name = 'mi_template.html'
```
Luego, debemos agregar la vista en el archivo `urls.py` del proyecto.

```python
from django.contrib import admin
from django.urls import path
from nombre_de_la_aplicacion.views import MiTemplateView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('mi_vista/', MiTemplateView.as_view(), name='mi_vista'),
]
```

# Clase 3 - 08/09/2016

## Implementación de Login y Registro en Django

### Configuración del sistema de autenticación

Django ya tiene un modelo de usuario (```django.contrib.auth.models.User```).

Ejecuta las migraciones iniciales para crear las tablas de autenticación en la base de datos:

``` bash
python manage.py migrate
```

Ahora, crea un superusuario para acceder al panel de administración:

```bash
python manage.py createsuperuser
```

Ingresa un nombre de usuario, correo y contraseña.

Ejecuta el servidor:

```bash
python manage.py runserver

```
Accede al panel en http://localhost:8000/admin/ e inicia sesión con el superusuario.

### Crear las vistas y formularios para el registro y login

Crea una aplicación llamada `accounts`:

```bash
python manage.py startapp accounts
```

Agrega la aplicación a `INSTALLED_APPS` en `settings.py`:

```python
INSTALLED_APPS = [
    ...
    'accounts',
    ...
]
```     
Crea un archivo `forms.py` en la carpeta de la aplicación `accounts` para definir los formularios de registro y login:

```python
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label="Contraseña")
    password_confirm = forms.CharField(widget=forms.PasswordInput, label="Confirmar Contraseña")

    class Meta:
        model = User
        fields = ['username', 'email']

    def clean_password_confirm(self):
        password = self.cleaned_data.get('password')
        password_confirm = self.cleaned_data.get('password_confirm')
        if password and password_confirm and password != password_confirm:
            raise ValidationError(_("Las contraseñas no coinciden"))
        return password_confirm

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user

class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Nombre de usuario")
    password = forms.CharField(widget=forms.PasswordInput, label="Contraseña")
``` 

Crea las vistas en `views.py` de la aplicación `accounts`:

```python
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import RegistrationForm, LoginForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registro exitoso. Ahora puedes iniciar sesión.")
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'accounts/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"Bienvenido, {username}!")
                return redirect('home')
            else:
                messages.error(request, "Nombre de usuario o contraseña incorrectos.")
    else:
        form = LoginForm()
    return render(request, 'accounts/login.html', {'form': form})

@login_required
def user_logout(request):
    logout(request)
    messages.info(request, "Has cerrado sesión.")
    return redirect('login')
```

### Configurar las URLs
Crea un archivo `urls.py` en la carpeta de la aplicación `accounts`:

```python
from django.urls import path
from .views import register, user_login, user_logout
urlpatterns = [
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
]
```

Luego, incluye las URLs de la aplicación `accounts` en el archivo `urls.py` del proyecto principal:

```python
from django.contrib import admin
from django.urls import path, include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
]
```

### Crear los templates para las vistas de registro y login
Dentro de `templates` que esta en la raíz de tu proyecto, crea otra carpeta llamada `accounts`. La estructura de carpetas debería verse así:

```
Proyecto/
    ├── templates/
    │   └── accounts/
    │       ├── login.html
    │       └── register.html
```
Crea el archivo `register.html`:

```html
<!-- templates/accounts/register.html -->
{% extends 'base.html' %}
{% block title %}Registro{% endblock %}

{% block content %}
<h2>Registro</h2>
<form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Registrar</button>
</form>
{% endblock %}
```
A lo mejor te preguntaras que es csrf_token, es un token de seguridad que previene ataques CSRF (Cross-Site Request Forgery).

Crea el archivo `login.html`:

```html
<!-- templates/accounts/login.html -->
{% extends 'base.html' %}
{% block title %}Iniciar Sesión{% endblock %}

{% block content %}
<h2>Iniciar Sesión</h2>
<form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Iniciar Sesión</button>
</form>
{% endblock %}
``` 
### Proteger vistas con login_required
Para proteger vistas y asegurarte de que solo los usuarios autenticados puedan acceder a ellas, utiliza el decorador `login_required` en las vistas que deseas proteger. Por ejemplo:

```python
from django.contrib.auth.decorators import login_required

@login_required
def perfil(request):
    return render(request, 'accounts/perfil.html')
```
Asegúrate de importar `login_required` desde `django.contrib.auth.decorators`.

### Configurar redirección después del login
En `settings.py`, puedes configurar la URL a la que se redirige a los usuarios después de iniciar sesión:

```python
LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = 'login'
```
Asegúrate de que `'home'` y `'login'` sean nombres de rutas válidos en tu proyecto.

