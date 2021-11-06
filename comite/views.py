from django.shortcuts import render
from django.views.generic import TemplateView
from django.utils.decorators import method_decorator        # Método decorador para usuario logueado y uso de la vista:
from django.contrib.auth.decorators import login_required   # Decorador para login requerido

# Cargamos el formulario de creacion de usuarios:
from django.urls import reverse_lazy                        # Función para redireccionar a una url
from django import forms      
       

# Create your views here.


class ComitePageView(TemplateView):
    
    template_name = 'comites/comite.html'
    
    
# Create your views here.
