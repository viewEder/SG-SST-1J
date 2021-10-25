from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView
from django.utils.decorators import method_decorator        # Método decorador para usuario logueado y uso de la vista:
from django.contrib.auth.decorators import login_required   # Decorador para login requerido
# Cargamos el Modelo de datos:
from .models import Profile
# Cargamos el formulario de creacion de usuarios:
from django.urls import reverse_lazy                        # Función para redireccionar a una url
from django import forms      
from .forms import ProfileForm          

# Create your views here.

# Creación de la vista para profile:
@method_decorator(login_required, name='dispatch')
class ProfilePageView(UpdateView):
    form_class = ProfileForm
    success_url = reverse_lazy('profile')
    template_name = 'registration/profile_form.html'
    
    def get_object(self):
        profile, created = Profile.objects.get_or_create(usuario = self.request.user)
        return profile