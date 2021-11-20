import datetime
from django.db import models
from django.db.models.base import Model
from datetime import date
from django.db.models.deletion import CASCADE
# from django.db.models.fields import CharField
from django.dispatch import receiver            # Libreria para hacer los cambios en los datos
from core.types.pandemia import Espandemia
from core.types.contrato import Contrato
from core.types.enfermedad import *
from core.types.medicamentos import *
# Create your models here.

class TipoEmpresa(models.Model):
    tipo_empresa = models.CharField(verbose_name='Tipo de Empresa', max_length=200, null=False, blank=False)
    create_at = models.DateField(auto_now_add=True, verbose_name="Creado el", null=True) 
    modify_at = models.DateField(auto_now=True, verbose_name="Actualizado el")

    class Meta:
        verbose_name = "Tipo de Empresa"
        verbose_name_plural = "Tipo de Empresa"

    def __str__(self) -> str:
        return self.tipo_empresa

class Empresa(models.Model): ## Clase que se usara para la creación de las empresas
    tipo = models.ForeignKey(TipoEmpresa,verbose_name="Tipo Empresa", on_delete=CASCADE)
    nombre = models.CharField(verbose_name='Nombre de Empresa', max_length=200, null=False, blank=False)
    nit = models.CharField(verbose_name='NIT', max_length=15, null=False, blank=False)
    actividad = models.CharField(verbose_name='Actividad Económica', max_length=255, null=False, blank=False)
    nivel_riesgo = models.CharField(verbose_name='Nivel de Riesgo', max_length=255)
    direccion = models.CharField(verbose_name='Dirección', max_length=255, null=False, blank=False)
    ciudad = models.CharField(verbose_name='Ciudad', max_length=255, blank=True, null=True)
    departamento = models.CharField(verbose_name='Departamento', max_length=255, blank=True, null=True)
    #cant_trabajadores = models.IntegerField(verbose_name='Cantidad de Trabajadores')
    naturaleza_empresa = models.CharField(verbose_name='Naturaleza jurídica', max_length=100, null=False, blank=False)
    telefonos = models.CharField(verbose_name='Teléfonos de contacto', max_length=40)
    correo = models.EmailField(verbose_name='Correo electrónico', max_length=255, null=False, blank=False)
    create_at = models.DateField(auto_now_add=True, verbose_name="Creado el", null=True)  
    modify_at = models.DateField(auto_now=True, verbose_name="Actualizado el")

    class Meta:
        verbose_name = 'Empresa'
        verbose_name_plural = 'Empresa'

    def __str__(self):
        return f'Nombre Empresa {self.nombre}'

class Areas(models.Model):## Clase que se usara para la creación de las áreas que tiene la empresa ingresada
    empresa = models.ForeignKey(Empresa, on_delete= CASCADE)
    nombre_area = models.CharField(verbose_name='Nombre Area', max_length= 255, null=False, blank=False)
    create_at = models.DateField(auto_now_add=True, verbose_name="Creado el", null=True)
    modify_at = models.DateField(auto_now=True, verbose_name="Actualizado el")
     
    class Meta:
        verbose_name = 'Nombre Area'
        verbose_name_plural = 'Areas de la empresa'

    def __str__(self):
        return f'Nombre Area {self.nombre_area}'


class NivelAcademico(models.Model):## Clase que se usara para la creación de los nieveles académicos o estudios de los empleados
    nivel = models.CharField(verbose_name='Nivel Académico', max_length= 255, null=False)
    create_at = models.DateField(auto_now_add=True, verbose_name="Creado el", null=True)
    modify_at = models.DateField(auto_now=True, verbose_name="Actualizado el")
     
    class Meta:
        verbose_name = 'Nivel Académico'
        verbose_name_plural = 'Niveles Académicos'

    def __str__(self):
        return f'Nivel Académico {self.nivel}'


class Cargos(models.Model):
    cargo = models.CharField(verbose_name='Cargo', max_length= 255, null=False)
    salario_cargo = models.IntegerField(verbose_name='Salario', default=0)    
    create_at = models.DateField(auto_now_add=True, verbose_name="Creado el", null=True)  
    modify_at = models.DateField(auto_now=True, verbose_name="Actualizado el")

    class Meta:
        verbose_name = 'Cargo'
        verbose_name_plural = 'Cargos'

    def __str__(self) -> str:
        return self.cargo


class Empleado(models.Model): ## Clase destinadad a la creación de los empleados
    codigo_empleado = models.CharField(verbose_name='Código de Empleado', max_length= 20, null=False)
    area = models.ForeignKey(Areas, on_delete=CASCADE)
    cargo = models.ForeignKey(Cargos, on_delete=CASCADE)
    nivel_academico = models.ForeignKey(NivelAcademico, on_delete=CASCADE)
    fecha_ingreso = models.DateField(verbose_name='Fecha de ingreso')
    salario_basico = models.DecimalField(verbose_name='Salario', max_digits=12, decimal_places=2)
    arl = models.CharField(verbose_name='ARL', max_length= 100, null=False)
    ssp = models.CharField(verbose_name='EPS', max_length= 100, null=False)
    sss = models.CharField(verbose_name='Fondo Pensiones', max_length= 100, null=False)
    ccf =  models.CharField(verbose_name='Caja de Compensación', max_length= 100, null=False, default="N/A")
    sufre_enfermedad = models.CharField(verbose_name="Sufre Alguna Enfermedad",max_length=255, choices=SufrEnfermedad, null=True)
    cual_enfermedad = models.CharField(verbose_name="Que enfermedad Sufre?",max_length=255, default="N/A")
    toma_medicamentos = models.CharField(verbose_name="Toma Medicamentos?",max_length=255, choices=TomaMedicamentos, null=True)
    cual_medicamento = models.CharField(verbose_name="Que Medicamento toma?",max_length=255, null=True, default="N/A")
    tipo_contrato = models.CharField(verbose_name="Tipo Contrato",max_length=255, choices=Contrato, null=True)
    #antiguedad = models.DecimalField(verbose_name="Tiempo en la empresa", max_digits=12, decimal_places=2,default=0)
    cuenta_bancaria =  models.CharField(verbose_name='Número de cuenta', max_length= 20, null=False)
    barrio = models.CharField(verbose_name="Barrio", max_length=255, null=True)
    ciudad = models.CharField(verbose_name="Ciudad", max_length=255, null=True)
    departamento = models.CharField(verbose_name="Departamento", max_length=255, null=True)
    estrato = models.IntegerField(verbose_name="Estrato", null=True, blank=True)
    fecha_retiro = models.DateField(verbose_name="Fecha de Retiro", auto_now=False, null=True)
    create_at = models.DateField(auto_now_add=True, verbose_name="Creado el", null=True)
    modify_at = models.DateField(auto_now=True, verbose_name="Actualizado el", null=True)


    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'

    def __str__(self):
        return f'Códgio Empleado  {self.codigo_empleado}'


class Responsabilidades(models.Model):
    responsabilidad = models.TextField(verbose_name='Responsabilidad', null=True, blank=True)
    create_at = models.DateField(auto_now_add=True, verbose_name="Creado el", null=True)
    modify_at = models.DateField(auto_now=True, verbose_name="Actualizado el")
     
    class Meta:
        verbose_name = 'Responsabiliad'
        verbose_name_plural = 'Responsabiliades'

    def __str__(self):
        return f'{self.responsabilidad[0:15]} (ver más)...'

class Capacitaciones(models.Model):
    pass


class Sanidad(models.Model):
    enfermedad = models.CharField(verbose_name="Tipo de Enfermedad",max_length=255)
    pandemia = models.CharField(verbose_name="Es Pandemia?",max_length=255, choices=Espandemia)## poner en un choicer
    create_at = models.DateField(auto_now_add=True, verbose_name="Creado el")
    modify_at = models.DateField(auto_now=True, verbose_name="Actualizado el")    

    class Meta:
        verbose_name = 'Sanidad (COVID-19 u otras)'
        verbose_name_plural = 'Sanidades (COVID-19 u otras)'

    def __str__(self):
        return f'{self.enfermedad}'

class DetalleSanidad(models.Model):
    empleado = models.ForeignKey(Empleado,on_delete=CASCADE)
    vacuna = models.CharField(verbose_name="Vacuna", max_length=144)
    dosis = models.IntegerField(verbose_name="Número Dosis", null=True, blank=True)
    fecha_dosis = models.DateField(verbose_name="Fecha de aplicación", auto_now=False)
    create_at = models.DateField(auto_now_add=True, verbose_name="Creado el")
    modify_at = models.DateField(auto_now=True, verbose_name="Actualizado el") 

    class Meta:
        verbose_name = 'Detalle Tratamiento'
        verbose_name_plural = 'Detalle Tratamientos'

    def __str__(self):
        return f'{self.empleado}'






         