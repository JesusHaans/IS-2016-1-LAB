"""
URL configuration for melodify project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path , include
from .views import listar_canciones, crear_libro, eliminar_cancion, editar_cancion

urlpatterns = [
    path('listar_canciones', listar_canciones, name = 'listar_canciones'),
    path('crear', crear_libro, name="crear_libro"),
    path('eliminar/<int:pk>', eliminar_cancion, name="eliminar_cancion"),
    path('editar/<int:pk>', editar_cancion, name="editar_cancion"),
    
    
]
