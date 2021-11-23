from django.db import models
from django.db.models.deletion import CASCADE
from empresa.models import Areas

# Create your models here.

#Modelo para almacenar las actividades de peligro
class ActividaesPeligro ( models.Model):
      process = models.CharField('Proceso', max_length=250, null=True, blank=True)
      area = models.ForeignKey(Areas, on_delete=CASCADE,null=True,blank=True, verbose_name="Area")
      routine = models.BooleanField('Es rutinario', default=False)
      description = models.TextField('Descripción', max_length=250, null=True, blank=True)
      created_at = models.DateField('Fecha de creación',auto_now_add=True)
      updated_at = models.DateField('Fecha de actualizacion', auto_now = True)
      status = models.BooleanField('Estado', default=False)

      class Meta:
            verbose_name = ('Actividad de peligro')
            verbose_name_plural = ('Actividaes de Peligro')

      def __str__(self):
            return "{0}".format(self.process)

#Modelo para almacenar las clasificaciones
class Clasificacion(models.Model):
      classification_name = models.CharField('Nombre', max_length=250, null=True, blank=True) 
      created_at = models.DateField('Fecha de creación',auto_now_add=True)
      updated_at = models.DateField('Fecha de actualizacion', auto_now = True)
      status = models.BooleanField('Estado', default=False)

      class Meta:
            verbose_name = ('Clasificacion')
            verbose_name_plural = ('Clasificaciones')

      def __str__(self):
            return "{0}".format(self.classification_name)

#Modelo para almacenar los efectos posibles
class EfectoPosible(models.Model):
      effects_name = models.CharField('Nombre', max_length=250, null=True, blank=True) 
      created_at = models.DateField('Fecha de creación',auto_now_add=True)
      updated_at = models.DateField('Fecha de actualizacion', auto_now = True)
      status = models.BooleanField('Estado', default=False)

      class Meta:
            verbose_name = ('Efecto Posible')
            verbose_name_plural = ('Efectos Posibles')

      def __str__(self):
            return "{0}".format(self.effects_name)

#Modelo para almacenar las fuentes
class Fuente(models.Model):
      source_name = models.CharField('Nombre', max_length=250, null=True, blank=True) 
      created_at = models.DateField('Fecha de creación',auto_now_add=True)
      updated_at = models.DateField('Fecha de actualizacion', auto_now = True)
      status = models.BooleanField('Estado', default=False)

      class Meta:
            verbose_name = ('Fuente')
            verbose_name_plural = ('Fuentes')

      def __str__(self):
            return "{0}".format(self.source_name)

#Modelo para almacenar los medios
class Medio(models.Model):
      medium_name = models.CharField('Nombre', max_length=250, null=True, blank=True) 
      created_at = models.DateField('Fecha de creación',auto_now_add=True)
      updated_at = models.DateField('Fecha de actualizacion', auto_now = True)
      status = models.BooleanField('Estado', default=False)

      class Meta:
            verbose_name = ('Medio')
            verbose_name_plural = ('Medios')

      def __str__(self):
            return "{0}".format(self.medium_name)


class ExamenMedico(models.Model):
      activitie_danger = models.ForeignKey(ActividaesPeligro, on_delete=CASCADE,null=True,blank=True, verbose_name="Actividades de peligro")
      classification = models.ForeignKey(Clasificacion, on_delete=CASCADE,null=True,blank=True, verbose_name="Clasificación")
      possible_effects = models.ForeignKey(EfectoPosible, on_delete=CASCADE,null=True,blank=True, verbose_name="Efectos Posibles")
      source = models.ForeignKey(Fuente, on_delete=CASCADE,null=True,blank=True, verbose_name="Fuente")
      medium = models.ForeignKey(Medio, on_delete=CASCADE,null=True,blank=True, verbose_name="Medio")
      individual  = models.CharField('Individuo', max_length=250, null=True, blank=True)
      deficiency_level = models.IntegerField('Nivel de deficiencia', default=0, null=True, blank=True)
      exposure_level = models.IntegerField('Nivel de exposición', default=0, null=True, blank=True)
      probability_level = models.IntegerField('Nivel de probabilidad', default=0, null=True, blank=True)
      probability_level_interpretation  = models.CharField('Interpretación nivel probabilidad', max_length=250, null=True, blank=True)
      consequence_level = models.IntegerField('Nivel de concecuencia', default=0, null=True, blank=True)
      risk_level = models.IntegerField('Nivel de riesgo', default=0, null=True, blank=True)
      risk_acceptance = models.IntegerField('Aceptación riesgo', default=0, null=True, blank=True)
      plant = models.IntegerField('Planta', default=0, null=True, blank=True)
      mission = models.IntegerField('Mision', default=0, null=True, blank=True)
      contractors = models.IntegerField('Contratistas', default=0, null=True, blank=True)
      practitioners = models.IntegerField('Practicantes', default=0, null=True, blank=True)
      risk_level_interpretation  = models.CharField('Interpretación nivel de riesgo', max_length=250, null=True, blank=True)
      worst_concecuence  = models.CharField('Peor concecuencia', max_length=250, null=True, blank=True)
      legal_requirement  = models.CharField('Existencia requisito legal', max_length=250, null=True, blank=True)
      elimination  = models.CharField('Eliminación', max_length=250, null=True, blank=True)
      substitution  = models.CharField('Sustitución', max_length=250, null=True, blank=True)
      engineering_control  = models.CharField('Control ingenieria', max_length=250, null=True, blank=True)
      administrator_control  = models.CharField('Control administrador', max_length=250, null=True, blank=True)
      equipment_elements_pp = models.CharField('Equipo elementos pp', max_length=250, null=True, blank=True)
      created_at = models.DateField('Fecha de creación',auto_now_add=True)
      updated_at = models.DateField('Fecha de actualizacion', auto_now = True)
      status = models.BooleanField('Estado', default=True)

      
      class Meta:
            verbose_name = ('Examen Medico')
            verbose_name_plural = ('Exámenes Médicos')

      def __str__(self):
            return "{0}".format(self.classification)

      
       
