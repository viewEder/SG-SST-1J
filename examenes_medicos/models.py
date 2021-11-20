from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.

#Modelo para almacenar las actividades de peligro
class ActividaesPeligro ( models.Model):
      process = models.CharField('Proceso', max_length=250, null=True, blank=True)
      area = models.CharField('Area', max_length=250, null=True, blank=True)
      routine = models.BooleanField('Es rutinario', default=False)
      description = models.CharField('Descripción', max_length=250, null=True, blank=True)
      created_at = models.DateField('Fecha de creación',auto_now_add=True)
      updated_at = models.DateField('Fecha de actualizacion', auto_now = True)
      status = models.BooleanField('Estado', default=False)

      class Meta:
            verbose_name = ('Actividaes Peligro')
            verbose_name_plural = ('Actividaes Peligros')

      def __str__(self):
            return "{0}".format(self.process)


class ExamenMedico(models.Model):
      classification = models.CharField('Clasificación', max_length=250, null=True, blank=True)
      sub_classification = models.CharField('Sub Clasificación', max_length= 250, null=True, blank=True)
      effects = models.CharField('Efectos posibles', max_length=250, null=True, blank=True)
      font = models.CharField('Fuentes', max_length=250, null=True, blank=True)
      middle = models.CharField('Medio', max_length=250, null=True, blank=True)
      individual  = models.CharField('Individuo', max_length=250, null=True, blank=True)
      nd = models.IntegerField('Nivel de deficiencia', default=0, null=True, blank=True)
      ne = models.IntegerField('Nivel de exposición', default=0, null=True, blank=True)
      np = models.IntegerField('Nivel de probabilidad', default=0, null=True, blank=True)
      inp  = models.CharField('Interpretación np', max_length=250, null=True, blank=True)
      nc = models.IntegerField('Nivel de concecuencia', default=0, null=True, blank=True)
      n_risk = models.IntegerField('Nivel de riesgo', default=0, null=True, blank=True)
      a_risk = models.IntegerField('Aceptación riesgo', default=0, null=True, blank=True)
      plant = models.IntegerField('Planta', default=0, null=True, blank=True)
      mission = models.IntegerField('Mision', default=0, null=True, blank=True)
      contractors = models.IntegerField('Contratistas', default=0, null=True, blank=True)
      practitioners = models.IntegerField('Practicantes', default=0, null=True, blank=True)
      inr  = models.CharField('Interpretación nr', max_length=250, null=True, blank=True)
      worst_concecuence  = models.CharField('Peor concecuencia', max_length=250, null=True, blank=True)
      e_requirement  = models.CharField('Existencia requisito legal', max_length=250, null=True, blank=True)
      elimination  = models.CharField('Eliminación', max_length=250, null=True, blank=True)
      substitution  = models.CharField('Sustitución', max_length=250, null=True, blank=True)
      c_ingenierie  = models.CharField('Control ingenieria', max_length=250, null=True, blank=True)
      c_admin  = models.CharField('Control administrador', max_length=250, null=True, blank=True)
      equipment_elements_pp = models.CharField('Equipo elementos pp', max_length=250, null=True, blank=True)
      created_at = models.DateField('Fecha de creación',auto_now_add=True)
      updated_at = models.DateField('Fecha de actualizacion', auto_now = True)
      status = models.BooleanField('Estado', default=True)
      activitie_danger = models.ForeignKey(ActividaesPeligro, on_delete=CASCADE)

      
      class Meta:
            verbose_name = ('Examen Medico')
            verbose_name_plural = ('Examenes Medicos')

      def __str__(self):
            return "{0}".format(self.classification)

      
       