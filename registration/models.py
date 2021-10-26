from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.db.models.expressions import OrderBy
from django.db.models.fields import CharField, IntegerField, TextField
from django.db.models.fields.related import ForeignKey, OneToOneField

# Create your models here.

#Con esta funcion nos aseguramos que el usuario suba la informacion requerida
def custom_upload_to(instance, filename):
    old_instance = Profile.objects.get(pk=instance.pk)
    old_instance.avatar.delete()
    return 'profiles/' + filename

class Profile(models.Model):
    usuario = models.OneToOneField(User, on_delete=CASCADE)
    avatar = models.ImageField(upload_to=custom_upload_to, null=True, blank=True)
    telefono = models.TextField(max_length=20)
    celular = models.TextField(max_length=20)
    direccion = models.TextField(max_length=255)
    profesion = models.TextField(max_length=255)

    class Meta:
        ordering = ['usuario__username']


