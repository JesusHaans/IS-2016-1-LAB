from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Cancion
from .forms import CancionForm

# Create your views here.
def listar_canciones(request):
    canciones_q = Cancion.objects.all()
    contexto = {"canciones": canciones_q}
    return render(request, "cancion/lista_canciones.html",contexto)

def crear_libro(request):
    if request.method == "POST":
        form = CancionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Cancion creada con éxito")
            return redirect("listar_canciones")
    else:
        form = CancionForm()
        contexto = {"form": form}
    return render(request, "cancion/crear_cancion.html", {"form": form})

def eliminar_cancion(request, pk):
    cancion = get_object_or_404(Cancion,pk=pk)
    if request.method == "POST":
        cancion.delete()
        messages.success(request, "Cancion eliminada con éxito")
        return redirect("listar_canciones")
    return render(request, "cancion/eliminar_cancion.html", {"cancion": cancion})

def editar_cancion(request, pk):
    cancion = get_object_or_404(Cancion, pk=pk)
    if request.method == "POST":
        form = CancionForm(request.POST, instance=cancion)
        if form.is_valid():
            form.save()
            messages.success(request, "Cancion actualizada con éxito")
            return redirect("listar_canciones")
    else:
        form = CancionForm(instance=cancion)
    return render(request, "cancion/editar_cancion.html", {"form": form})