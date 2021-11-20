from django.db import models
from core.types.Pvha import Phva





class EstructuraPlanAnual(models.Model): ## Clase que se usara para la estructura del plan anual
        nombre= models.CharField(verbose_name="Nombre de la estructura",max_length=40, null=True, blank=True)          
        activo=models.BooleanField(verbose_name='Activo')
        create_at = models.DateField(auto_now_add=True, verbose_name="Creado el", null=True)  
        modify_at = models.DateField(auto_now=True, verbose_name="Actualizado el")

        class Meta:
            verbose_name = 'Estrutura Plan anual'
            verbose_name_plural = 'Estructura plan anual'

        def __str__(self):
            return f'Nombre Empresa {self.nombre}'             

class EquipoResponsable(models.Model): ## Clase que se usara para la creación de las empresas
        nombre_equipo= models.CharField(verbose_name='Nombre del eqiupo', max_length=40)        
        activo=models.BooleanField(verbose_name='Activo')
        create_at = models.DateField(auto_now_add=True, verbose_name="Creado el", null=True)  
        modify_at = models.DateField(auto_now=True, verbose_name="Actualizado el")

        class Meta:
            verbose_name = 'Equipo Responsable'
            verbose_name_plural = 'Equipo Responsable'

        def __str__(self):
            return f'Nombre Empresa {self.nombre_equipo}'  

class PlanAnual(models.Model): ## Clase que se usara para la creación de las empresas
        anio = models.IntegerField(verbose_name="Año", null=True, blank=True)
        objetivo= models.TextField(verbose_name='Objetivo', max_length=1000) 
        metas= models.TextField(verbose_name='Metas', max_length=1000) 
        alcance= models.TextField(verbose_name='Alcance', max_length=1000)        
        nombre_archivo = models.CharField(verbose_name="Nombre del archivo", max_length=100)
        activo=models.BooleanField(verbose_name='Activo')
        create_at = models.DateField(auto_now_add=True, verbose_name="Creado el", null=True)  
        modify_at = models.DateField(auto_now=True, verbose_name="Actualizado el")

        class Meta:
            verbose_name = 'Plan anual'
            verbose_name_plural = 'Plan anual'

        def __str__(self):
            return f'Nombre Empresa {self.objetivo}'

class ActividadesPlan(models.Model): ## Clase que se usara para la creación del plan de actividades ssgt
        plan = models.ForeignKey(PlanAnual, verbose_name='Plan Anual',on_delete=models.CASCADE)
        estructura = models.ForeignKey(EstructuraPlanAnual, verbose_name='Identificacion de la estructura',on_delete=models.CASCADE)
        equipo_responsable= models.ForeignKey(EquipoResponsable, verbose_name='Identificion del equipo responsable', on_delete=models.CASCADE)
        etapa_phva= models.CharField(verbose_name='Etapa del phva',  choices=Phva,max_length=40, null=False, blank=False)
        actividad= models.TextField(verbose_name='Actividades del plan anual', max_length=15, null=False, blank=False)        
        recursos= models.CharField(verbose_name='Recursos del plan anual', max_length=255)
        fuente_informacion = models.CharField(verbose_name='Fuente de informacion del plan anual', max_length=255, null=False, blank=False)
        # Pendiente de modelo
        #periodicidad= models.ForeignKey(verbose_name='Periodicidad del pan anual', on_delete=models.CASCADE)
        fecha_planeacion= models.DateField(auto_now_add=True, verbose_name="Fecha de planeacion", null=True)              
        estado_actividad= models.IntegerField(verbose_name='Estado de actividad', null=False, blank=False)
        nombre_archivo= models.CharField(verbose_name='Interpretacion de resultados', max_length=40)
       
        create_at = models.DateField(auto_now_add=True, verbose_name="Creado el", null=True)  
        modify_at = models.DateField(auto_now=True, verbose_name="Actualizado el")

        class Meta:
            verbose_name = 'Plan de actividades'
            verbose_name_plural = 'Plan de actividades'

        def __str__(self):
            return f'Nombre Empresa {self.plan}'  



class CumplimientoPlanAnual(models.Model): ## Clase que se usara para el cumplimiento de plana anual
        actividad= models.ForeignKey(ActividadesPlan, verbose_name="Nombre de la actividad", on_delete=models.CASCADE)
        mes= models.IntegerField(verbose_name='Mes de la actividad,max_length=2') 
        porcentaje_cumplimiento= models.TextField(verbose_name='Metas', max_length=3) 
        fecha_cumplimiento= models.DateField(auto_now_add=True, verbose_name="Fecha de cumplimiento", null=True) 
        nombre_archivo = models.CharField(verbose_name="Nombre del archivo", max_length=100)        
        activo=models.BooleanField(verbose_name='Activo')
        create_at = models.DateField(auto_now_add=True, verbose_name="Creado el", null=True)  
        modify_at = models.DateField(auto_now=True, verbose_name="Actualizado el")

        class Meta:
            verbose_name = 'Cumplimiento Plan anual'
            verbose_name_plural = 'Ejecucion de actividades'

        def __str__(self):
            return f'Nombre Empresa {self.actividad}'
            
            

# Create your models here.
