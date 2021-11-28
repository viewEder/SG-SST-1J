from django.db import models
from core.types.tipo_ind import tipo_ind

 

class TipoIndicador(models.Model): ## Clase que se usara para la creación de los indicadores delsgsst
    tipo_indicador = models.CharField(verbose_name='Tipo de indicador',max_length=15, choices= tipo_ind, null=False, blank=False)        
    create_at = models.DateField(auto_now_add=True, verbose_name="Creado el", null=True)  
    modify_at = models.DateField(auto_now=True, verbose_name="Actualizado el")

    class Meta:
        verbose_name = 'Tipo de Indicador'
        verbose_name_plural = 'Tipo de indicador indicador'

    def __str__(self):
        return f'Nombre Empresa {self.tipo_indicador}'    

class Indicadores(models.Model): ## Clase que se usara para la creación de los indicadores delsgsst
    tipo_indicador = models.ForeignKey(TipoIndicador, on_delete= models.CASCADE)
    nombre = models.CharField(verbose_name='Nombre del indicador', max_length=200, null=False, blank=False)
    definicion= models.CharField(verbose_name='Definicion del indicador', max_length=15, null=False, blank=False)
    metodo_calculo= models.CharField(verbose_name='Metodo de calculo', max_length=255, null=False, blank=False)
    unidad_medidad = models.CharField(verbose_name='Unidad de medida', max_length=255)
    fuente_informacion = models.CharField(verbose_name='Fuente de informacion', max_length=255, null=False, blank=False)
    clasificacion= models.CharField(verbose_name='CLasificacion', max_length=255, blank=True, null=True)
    frecuencia_medicion= models.CharField(verbose_name='Frecuencia de medicion', max_length=255, blank=True, null=True)       
    meta_anual= models.IntegerField(verbose_name='Meta anual', null=False, blank=False)
    Interpretacion_resultados= models.CharField(verbose_name='Interpretacion de resultados', max_length=40)
    responsable = models.CharField(verbose_name='responsable', max_length=255, null=False, blank=False)
    deben_conocer_resultado= models.CharField(verbose_name='Deben de conocer el resultaddo', max_length=100, null=False, blank=False)
    activo=models.BooleanField(verbose_name='Activo', default=False)
    create_at = models.DateField(auto_now_add=True, verbose_name="Creado el", null=True)  
    modify_at = models.DateField(auto_now=True, verbose_name="Actualizado el")

    class Meta:
        verbose_name = 'Indicador'
        verbose_name_plural = 'indicador'

    def __str__(self):
        return f'Nombre Empresa {self.tipo_indicador}'
            
        
            