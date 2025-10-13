from django.shortcuts import render, redirect # me falto importar esto por eso no funcionaba mi redirect :P
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView

# Create your views here.

#def home(request):
#    return HttpResponse("<h1> Hola Mundo </h1>")

class HomeView( TemplateView):
    template_name = 'inicio_sesion/home.html'

class CustomLoginView(LoginView):
    template_name = 'registration/login.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')  # o 'dashboard'
        return super().dispatch(request, *args, **kwargs)