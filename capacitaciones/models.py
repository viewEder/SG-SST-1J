from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ForeignKey
from core.types.meses import Meses

# Create your models here.

# class Plan_Capacitacion(models.Model):
#     #periodo = models.ForeignKey(Periodo, on_delete=CASCADE)
#     justificacion = models.CharField(verbose_name="Justificacion", max_length=255)
#     alcance = models.CharField(verbose_name="Alcance", max_length=255)
#     objetivo = models.CharField(verbose_name="Objetivo", max_length=255)
#     indicadores = models.CharField(verbose_name="Indicadores", max_length=255)
#     create_at = models.DateField(auto_now_add=True, verbose_name="Creado el", null=True)  
#     modify_at = models.DateField(auto_now=True, verbose_name="Actualizado el")

#     class Meta:
#         verbose_name_plural = 'Plan de Capacitacion'

# #Con esta funcion nos aseguramos que el usuario suba la informacion requerida
# def soporte_capacitacion_upload_to(instance, filename):
#     old_instance = Capacitaciones.objects.get(pk=instance.pk)
#     old_instance.avatar.delete()
#     return 'recursos/capacitaciones/' + filename

# class Capacitaciones(models.Model):
#     id_capacitacion = models.ForeignKey(Plan_Capacitacion, on_delete=CASCADE)
#     tema = models.CharField(verbose_name="Tema", max_length=255)
#     area = models.CharField(verbose_name="Area del Empleado", max_length=255)
#     responsable = models.CharField(verbose_name="Responsable", max_length=255)
#     meses = models.CharField(verbose_name="Estado Civil", max_length=20, choices=Meses)
#     archivo_soporte = models.FieldFile(upload_to=soporte_capacitacion_upload_to, null=True, blank=True)
#     fecha_planeacion = models.DateField(verbose_name="Fecha de Planeacion")
#     fecha_cumplimiento = models.DateField(verbose_name="Fecha de Cumplimiento")
#     create_at = models.DateField(auto_now_add=True, verbose_name="Creado el", null=True)  
#     modify_at = models.DateField(auto_now=True, verbose_name="Actualizado el")

#     class Meta:
#         verbose_name_plural = 'Capacitaciones'

