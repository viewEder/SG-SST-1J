from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.db.models.expressions import OrderBy
from django.db.models.fields import CharField, IntegerField, TextField
from django.db.models.fields.related import ForeignKey, OneToOneField
from core.types.generos import Generos
from core.types.estacivil import EstaCivil
from core.types.parentesco import Parentesco
from django.dispatch import receiver    # Libreria para hacer los cambios en los datos
from django.db.models.signals import post_save  # Complemento de dispatch

# Create your models here.

#Con esta funcion nos aseguramos que el usuario suba la informacion requerida
def custom_upload_to(instance, filename):
    old_instance = Profile.objects.get(pk=instance.pk)
    old_instance.avatar.delete()
    return 'profiles/' + filename

class Profile(models.Model):
    usuario = models.OneToOneField(User, on_delete=CASCADE)
    avatar = models.ImageField(upload_to=custom_upload_to, null=True, blank=True)
    telefono = models.CharField(max_length=20, verbose_name="Telefono", null=True, blank=True)
    celular = models.CharField(max_length=20, verbose_name="Celular", null=True, blank=True)
    direccion = models.CharField(max_length=255,verbose_name="Direccion", null=True, blank=True)
    profesion = models.CharField(max_length=255,verbose_name="Profesion", null=True, blank=True)
    cedula = models.CharField(max_length=20,verbose_name="Cedula", null=True, blank=True)
    genero = models.CharField(max_length=20, choices=Generos,verbose_name="Genero",default="Otro")
    fecha_nacimiento = models.DateField(verbose_name="Fecha Nacimiento", null=False,blank=False)
    estado_civil = models.CharField(max_length=20, choices=EstaCivil,verbose_name="Estado Civil",default="No indica")
    create_at = models.DateField(auto_now_add=True, verbose_name="Creado el", null=True)  
    modify_at = models.DateField(auto_now=True, verbose_name="Actualizado el")
    
    class Meta:
        ordering = ['usuario__username']
    
    def __str__(self):
        return f(self.usuario)

# Función exclusiva para los usuarios logueados:
@receiver(post_save, sender=User)
def ensure_profile_exists(sender, instance, **kwargs):
    if kwargs.get('created', False):
        Profile.objects.get_or_create(usuario=instance)


class Contacto_Emergencia(models.Model):
    usuario = models.ForeignKey(User, on_delete=CASCADE)
    contacto_emergencia = models.CharField(max_length=255, verbose_name="Contacto Emergencia", null=True, blank=True)
    parentesco_emergercia = models.CharField(max_length=20, choices=Parentesco,verbose_name="Parentesco", null=True, blank=True)
    telefono_emergencia = models.CharField(max_length=20, verbose_name="Telefono Emergencia", null=True, blank=True)
    create_at = models.DateField(auto_now_add=True, verbose_name="Creado el", null=True)  
    modify_at = models.DateField(auto_now=True, verbose_name="Actualizado el")

    class Meta:
        ordering = ['usuario__username']
    
    def __str__(self):
        return self.usuario