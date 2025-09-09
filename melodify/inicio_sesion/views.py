from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

# Create your views here.

#def home(request):
#    return HttpResponse("<h1> Hola Mundo </h1>")

class HomeView(TemplateView):
    template_name = 'inicio_sesion/home.html'