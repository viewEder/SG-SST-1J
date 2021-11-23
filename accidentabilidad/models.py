from django.db import models
from empresa.models import Empleado
from django.db.models.deletion import CASCADE

# Create your models here.

#Modelo para almacenar los peligros
class Peligro(models.Model):
    danger_name = models.CharField('Nombre',max_length=250, blank=True, null=True)
    created_at = models.DateField('Fecha de creación',auto_now_add=True)
    updated_at = models.DateField('Fecha de actualización', auto_now = True)
    status = models.BooleanField('Estado', default=False)

    class Meta:
        verbose_name = ('Peligro')
        verbose_name_plural = ('Peligros')

    def __str__(self):
        return "{0}".format(self.name)

#Modelo para almacenar los tipos de accidentes
class TipoAccidente(models.Model):
    accident_type_name = models.CharField('Nombre',max_length=250, blank=True, null=True)
    created_at = models.DateField('Fecha de creación',auto_now_add=True)
    updated_at = models.DateField('Fecha de actualizacion', auto_now = True)
    status = models.BooleanField('Estado', default=False)

    class Meta:
        verbose_name = ('Tipo de Accidente')
        verbose_name_plural = ('Tipos de Accidentes')

    def __str__(self):
        return "{0}".format(self.name)

#Modelo para almacenar las partes del cuerpo afectadas
class ParteDelCuerpo(models.Model):
    body_part_name = models.CharField('Nombre',max_length=250, blank=True, null=True)
    created_at = models.DateField('Fecha de creación',auto_now_add=True)
    updated_at = models.DateField('Fecha de actualización', auto_now = True)
    status = models.BooleanField('Estado', default=False)

    class Meta:
        verbose_name = ('Parte del Cuerpo')
        verbose_name_plural = ('Partes del Cuerpo afectadas')

    def __str__(self):
        return "{0}".format(self.name)

#Modelo para almacenar el mecanismo de accidentes
class MecanismoAccidente(models.Model):
    mechanism_name = models.CharField('Nombre',max_length=250, blank=True, null=True)
    created_at = models.DateField('Fecha de creación',auto_now_add=True)
    updated_at = models.DateField('Fecha de actualización', auto_now = True)
    status = models.BooleanField('Estado', default=False)

    class Meta:
        verbose_name = ('Mecanismo de Accidente')
        verbose_name_plural = ('Mecanismos de Accidentes')

    def __str__(self):
        return "{0}".format(self.name)

#Modelo para almacenar los agentes de accidentes 
class AgenteAccidente(models.Model):
    agent_name = models.CharField('Nombre',max_length=250, blank=True, null=True)
    created_at = models.DateField('Fecha de creación',auto_now_add=True)
    updated_at = models.DateField('Fecha de actualización', auto_now = True)
    status = models.BooleanField('Estado', default=False)

    class Meta:
        verbose_name = ('Agente de Accidente')
        verbose_name_plural = ('Agentes de Accidentes')

    def __str__(self):
        return "{0}".format(self.name)

#Modelo para almacenar los tipos de lecciones 
class TipoLeccion(models.Model):
    lesson_ame = models.CharField('Nombre',max_length=250, blank=True, null=True)
    created_at = models.DateField('Fecha de creación',auto_now_add=True)
    updated_at = models.DateField('Fecha de actualizacion', auto_now = True)
    status = models.BooleanField('Estado', default=False)

    class Meta:
        verbose_name = ('Tipo de Leccion')
        verbose_name_plural = ('Tipos de Lecciones')

    def __str__(self):
        return "{0}".format(self.name)

#Modelo para almacenar las causas basicas de accidentes
class CausaBasica(models.Model):
    cause_name = models.CharField('Nombre',max_length=250, blank=True, null=True)
    created_at = models.DateField('Fecha de creación',auto_now_add=True)
    updated_at = models.DateField('Fecha de actualizacion', auto_now = True)
    status = models.BooleanField('Estado', default=False)

    class Meta:
        verbose_name = ('Causa Basica')
        verbose_name_plural = ('Causas Basicas')

    def __str__(self):
        return "{0}".format(self.name)

#Modelo para almacenar las causas inmediatas de accidentes
class CausaInmediata(models.Model):
    immediate_cause_name = models.CharField('Nombre',max_length=250, blank=True, null=True)
    created_at = models.DateField('Fecha de creación',auto_now_add=True)
    updated_at = models.DateField('Fecha de actualizacion', auto_now = True)
    status = models.BooleanField('Estado', default=False)

    class Meta:
        verbose_name = ('Causa Inmediata')
        verbose_name_plural = ('Causas Inmediatas')

    def __str__(self):
        return "{0}".format(self.name)





class Accidentabilidad(models.Model):
    empleado = models.ForeignKey(Empleado,on_delete=CASCADE,null=True,blank=True, verbose_name="Empleado")
    peligro = models.ForeignKey(Peligro,on_delete=CASCADE,null=True,blank=True, verbose_name="Peligro")
    accident_type = models.ForeignKey(TipoAccidente,on_delete=CASCADE,null=True,blank=True, verbose_name="Tipo accidente")
    part_body_affected = models.ForeignKey(ParteDelCuerpo,on_delete=CASCADE,null=True,blank=True, verbose_name="Parte afectada")
    accident_mechanism = models.ForeignKey(MecanismoAccidente,on_delete=CASCADE,null=True,blank=True, verbose_name="Mecanismo del accidente")
    accident_agent = models.ForeignKey(AgenteAccidente,on_delete=CASCADE,null=True,blank=True, verbose_name="Agente accidente")
    lesion_type = models.ForeignKey(TipoLeccion,on_delete=CASCADE,null=True,blank=True, verbose_name="Tipo lección")
    basic_cause = models.ForeignKey(CausaBasica,on_delete=CASCADE,null=True,blank=True, verbose_name="Causa básica")
    immediate_cause = models.ForeignKey(CausaInmediata,on_delete=CASCADE,null=True,blank=True, verbose_name="Causa inmediata")


    date = models.DateTimeField('Fecha',auto_now_add=True)
    cie10 = models.CharField('Cie 10', max_length=250, null=True, blank=True)
    diagnosis = models.CharField('Diagnóstico', max_length=255, null=True, blank=True)
    inability_days = models.IntegerField('Días de incapacidad', default=0, null=True, blank=True)
    intervention_measure = models.CharField('Medida intervención', max_length=255, null=True, blank=True)
    compliance = models.IntegerField('Cumplimiento', default=0, null=True, blank=True)
    accident_description = models.TextField('Descripción accidente', max_length=255, null=True, blank=True)
    created_at = models.DateField('Fecha de creación',auto_now_add=True)
    updated_at = models.DateField('Fecha de actualización', auto_now = True)
    status = models.BooleanField('Estado', default=False)

    class Meta:
        verbose_name = ('Accidentabilidad')
        verbose_name_plural = ('Accidentabilidades')

    def __str__(self):
        return "{0}".format(self.empleado)


