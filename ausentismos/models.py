import datetime
from django.db import models
from empresa.models import Empleado
from django.db.models.base import Model
from datetime import date
from django.db.models.deletion import CASCADE
#from django.db.models.fields import _ChoiceNamedGroup


# Create your models here.

class Cie10(models.Model):
    diagnostico = models.CharField(verbose_name="Código CIE 10", max_length=4)
    grupo = models.TextField(verbose_name="Grupo de Diagnóstico")
    descripcion = models.TextField(verbose_name="Descripción de Diagnóstico")

    class Meta:
        verbose_name = 'Diagnostico'
        verbose_name_plural = 'Diagnosticos'

    def __str__(self):
        return f'Diagnóstico {self.diagnostico}'

class Incapacidades(models.Model):
    empleado = models.ForeignKey(Empleado, on_delete= CASCADE, default=1)
    mes  = models.CharField(verbose_name="Mes", max_length=30)
    origen = models.CharField(verbose_name="Origen", max_length=155)
    clasificacion = models.CharField(verbose_name="Clasificación", max_length=155)
    fecha_inicio = models.DateField(verbose_name="Fecha de Inicio", auto_now=False)
    fecha_fin = models.DateField(verbose_name="Fecha de Finalzaición", auto_now=False)
    total_incapacidad = models.IntegerField(verbose_name="Total días incapacidad")
    valor_incapacidad = models.DecimalField(verbose_name="Valor Incapacidad", decimal_places=2, max_digits=12)
    valor_asumido_empresa = models.DecimalField(verbose_name="Valor Asumido Empresa", decimal_places=2, max_digits=12)
    valor_asumido_eps = models.DecimalField(verbose_name="Valor Asumido EPS", decimal_places=2, max_digits=12)
    create_at = models.DateField(auto_now_add=True, verbose_name="Creado el")
    modify_at = models.DateField(auto_now=True, verbose_name="Actualizado el")

    class Meta:
        verbose_name = 'Registro Incapacidad'
        verbose_name_plural = 'Registro Incapacidades'

    def __str__(self):
        return f'Incapacidad {self.clasificacion}'