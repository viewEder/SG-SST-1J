from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE
from .models import * 
from empresa.models import Empleado

# Create your models here.


class Comite(models.Model): # Clase que se usara para la creación del comite
    nombcomite = models.CharField(verbose_name='Nombre de Comite', max_length=200, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    class Meta:
        verbose_name = 'Comite'
        verbose_name_plural = 'Comite'

    def __str__(self):
        return self.nombcomite

       
class RolComite(models.Model): # Clase que se usara para la creación del comite
    tipo_rol = models.CharField(verbose_name='Rol de Comite', max_length=200, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'Rol Comite'
        verbose_name_plural = 'Rol Comite'

    def __str__(self):
        return self.tipo_rol       


class ParticipantesComite(models.Model): # Clase que se usara para la creación del comite
    comite_id = models.ForeignKey(Comite, on_delete=models.CASCADE)
    rol_comite = models.ForeignKey(RolComite, on_delete=models.CASCADE)
    empleados=models.ForeignKey(Empleado, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    