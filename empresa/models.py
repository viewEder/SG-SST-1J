from django.db import models
from django.db.models.base import Model

from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField
from django.dispatch import receiver            # Libreria para hacer los cambios en los datos
# Create your models here.

class Empresa(models.Model): ## Clase que se usara para la creación de las empresas
    nombre = models.CharField(verbose_name='Nombre de Empresa', max_length=200, null=False, blank=False)
    nit = models.CharField(verbose_name='NIT', max_length=15, null=False, blank=False)
    actividad = models.CharField(verbose_name='Actividad Económica', max_length=255, null=False, blank=False)
    nivel_riesgo = models.CharField(verbose_name='Nivel de Riesgo', max_length=255)
    direccion = models.CharField(verbose_name='Dirección', max_length=255, null=False, blank=False)
    ciudad = models.CharField(verbose_name='Ciudad', max_length=255, null=False, blank=False)
    departamento = models.CharField(verbose_name='Departamento', max_length=255, null=False, blank=False)
    #cant_trabajadores = models.IntegerField(verbose_name='Cantidad de Trabajadores')
    naturaleza_empresa = models.CharField(verbose_name='Naturaleza jurídica', max_length=100, null=False, blank=False)
    telefonos = models.CharField(verbose_name='Teléfonos de contacto', max_length=40)
    correo = models.EmailField(verbose_name='Correo electrónico', max_length=255, null=False, blank=False)
    tipo = models.CharField(verbose_name='Tipo de empresa', max_length=100, null=False, blank=False)

    class Meta:
        verbose_name = 'Empresa'
        verbose_name_plural = 'Empresa'

    def __str__(self):
        return f'Nombre Empresa {self.nombre}'

class Areas(models.Model):## Clase que se usara para la creación de las áreas que tiene la empresa ingresada
    nombre_area = models.CharField(verbose_name='Nombre Area', max_length= 255, null=False, blank=False)
    nit_empresa = models.ForeignKey(Empresa, on_delete= CASCADE)

    class Meta:
        verbose_name = 'Nombre Area'
        verbose_name_plural = 'Areas de la empresa'

    def __str__(self):
        return f'Nombre Area {self.nombre_area}'

class NivelAcademico(models.Model):## Clase que se usara para la creación de los nieveles académicos o estudios de los empleados
    nivel = models.CharField(verbose_name='Nivel Académico', max_length= 255, null=False)

    class Meta:
        verbose_name = 'Nivel Académico'
        verbose_name_plural = 'Niveles Académicos'

    def __str__(self):
        return f'Nivel Académico {self.nivel}'

class Cargos(models.Model):
    cargo = models.CharField(verbose_name='Cargo', max_length= 255, null=False)
    salario_cargo = models.IntegerField(verbose_name='Salario')

    class Meta:
        verbose_name = 'Cargo'
        verbose_name_plural = 'Cargos'

<<<<<<< HEAD
    def __str__(self) -> str:
        return self.cargo
=======
    def __str__(self):
        return f'Cargo {self.cargo}'
>>>>>>> 010de1c77b81c8902a7f498187e7e53c406fd2b7

class Empleado(models.Model): ## Clase destinadad a la creación de los empleados
    codigo_empleado = models.CharField(verbose_name='Código de Empleado', max_length= 20, null=False)
    area = models.ForeignKey(Areas, on_delete=CASCADE)
    cargo = models.ForeignKey(Cargos, on_delete=CASCADE)
    nivel_academico = models.ForeignKey(NivelAcademico, on_delete=CASCADE)
    fecha_ingreso = models.DateField(verbose_name='Fecha de ingreso')
    salario_basico = models.IntegerField(verbose_name='Salario')
    arl = models.CharField(verbose_name='ARL', max_length= 100, null=False)
    ssp = models.CharField(verbose_name='EPS', max_length= 100, null=False)
    sss = models.CharField(verbose_name='Fondo Pensiones', max_length= 100, null=False)
    cuenta_bancaria =  models.CharField(verbose_name='Número de cuenta', max_length= 20, null=False)

    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'

    def __str__(self):
        return f'Códgio Empleado  {self.codigo_empleado}'