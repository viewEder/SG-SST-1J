import datetime
from django.db import models
from django.db.models.base import Model, ModelStateFieldsCacheDescriptor
from datetime import date
from django.db.models.deletion import CASCADE
from django.db.models.expressions import ValueRange
from empresa.models import Empleado 
from proveedor.models import Proveedor

# Create your models here.


class Periodo(models.Model):
    anio = models.IntegerField(verbose_name="Año")
    create_at = models.DateField(auto_now_add=True, verbose_name="Creado el")
    modify_at = models.DateField(auto_now=True, verbose_name="Actualizado el")

    class Meta:
        verbose_name = 'Periodo'
        verbose_name_plural = 'Periodo Presupuestal'

    def __str__(self):
        return f'Año {self.anio}'


class EjecucionPresupuesto(models.Model):
    id_proveedor = models.ForeignKey(Proveedor,on_delete=CASCADE) 
    fecha = models.DateField(verbose_name="Fecha", auto_now=False, null=True)
    factura = models.CharField(verbose_name="Factura", max_length=255, null=False)
    cantidad = models.DecimalField(verbose_name="Cantidad", max_digits=15, decimal_places=2)
    valor_sin_iva = models.DecimalField(verbose_name="Valor Sin IVA", max_digits=12, decimal_places=2)
    valor_iva = models.DecimalField(verbose_name="Valor IVA", max_digits=15, decimal_places=2)
    valor_total = models.DecimalField(verbose_name="Valor Total", max_digits=15, decimal_places=2)
    total = models.DecimalField(verbose_name="Valor Total", max_digits=15, decimal_places=2)
    activo = models.BooleanField(verbose_name="Activo", default=True)
    create_at = models.DateField(auto_now_add=True, verbose_name="Creado el")
    modify_at = models.DateField(auto_now=True, verbose_name="Actualizado el")

    class Meta:
        verbose_name = 'Ejecucion presupuestal'
        verbose_name_plural = 'Ejecuciones presupuestales'

    def __str__(self):
        return self.factura


class CronogramaPresupuesto(models.Model):  
    periodo = models.ForeignKey(Periodo, verbose_name="Periodo", on_delete=CASCADE)
    actividad = models.CharField(verbose_name="Actividad", max_length=255)
    observaciones = models.TextField(verbose_name="Observaciones")
    responsable = models.CharField(verbose_name="Responsable", max_length=255)
    presupuesto =models.DecimalField(verbose_name="Presupuesto", max_digits=15, decimal_places=2) 
    create_at = models.DateField(auto_now_add=True, verbose_name="Creado el")
    modify_at = models.DateField(auto_now=True, verbose_name="Actualizado el")
    activo = models.BooleanField(verbose_name="Activo", default=True)
    class Meta:
        verbose_name = 'Actividad'
        verbose_name_plural = 'Plan de Actividades'

    def __str__(self):
        return self.actividad