from django.db import models
from empresa.models import Empleado
from django.db.models.deletion import CASCADE

# Create your models here.

#Modelo para almacenar los peligros
class Peligro(models.Model):
    name = models.CharField(max_length=250, blank=True, null=True)
    created_at = models.DateField('Fecha de creación',auto_now_add=True)
    updated_at = models.DateField('Fecha de actualizacion', auto_now = True)
    status = models.BooleanField('Estado', default=False)

    class Meta:
        verbose_name = ('Peligro')
        verbose_name_plural = ('Peligros')

    def __str__(self):
        return "{0}".format(self.name)


class Accidentabilidad(models.Model):
    date = models.DateTimeField('Fecha',auto_now_add=True)
    inability_days = models.IntegerField('Practicantes', default=0, null=True, blank=True)
    cie10 = models.CharField('Cie 10', max_length=250, null=True, blank=True)
    diagnosis = models.CharField('Diagnóstico', max_length=255, null=True, blank=True)
    accident_description = models.TextField('Descripcion accidente', max_length=255, null=True, blank=True)
    accident_type = models.CharField('Tipo accidente', max_length=255, null=True, blank=True)
    part_body_affected = models.CharField('Parte del cuerpo afectada', max_length=255, null=True, blank=True)
    accident_mechanism = models.CharField('Mecanismo accidente', max_length=255, null=True, blank=True)
    accident_agent = models.CharField('Agente accidente', max_length=255, null=True, blank=True)
    lesion_type = models.CharField('Tipo de lección', max_length=255, null=True, blank=True)
    basic_cause = models.CharField('Causa básica', max_length=255, null=True, blank=True)
    immediate_cause = models.CharField('Causa inmediata', max_length=255, null=True, blank=True)
    intervention_measure = models.CharField('Medida intervención', max_length=255, null=True, blank=True)
    compliance = models.CharField('Cumplimiento', max_length=255, null=True, blank=True)
    created_at = models.DateField('Fecha de creación',auto_now_add=True)
    updated_at = models.DateField('Fecha de actualizacion', auto_now = True)
    status = models.BooleanField('Estado', default=False)
    empleado = models.ForeignKey(Empleado,on_delete=CASCADE)
    peligro = models.ForeignKey(Peligro,on_delete=CASCADE)

    class Meta:
        verbose_name = ('Accidentabilidad')
        verbose_name_plural = ('Accidentabilidades')

    def __str__(self):
        return "{0}".format(self.empleado)


