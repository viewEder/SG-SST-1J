from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import OneToOneField
from empresa.models import Empleado, Empresa
from comite.models import Comite



#Modelo para almacenar los tipos de documentos
class TipoDocumento(models.Model):
    name = models.CharField('Nombre', max_length= 250, null=True, blank=True)
    created_at = models.DateField('Fecha de creación',auto_now_add=True)
    updated_at = models.DateField('Fecha de actualizacion', auto_now = True)
    status = models.BooleanField('Estado', default=True)
    

    class Meta:
        verbose_name = 'Tipo Documento'
        verbose_name_plural = 'Tipo Documentos'

    def __str__(self):
        return self.name

#Con esta funcion nos aseguramos que el usuario suba la informacion requerida
def upload_documentos_empleado(instance, filename):
    return 'recursos/empleado/' + filename

#Modelo para almacenar documentos de los empleados
class DocumentosEmpleado(models.Model):
    empleado = models.ForeignKey(Empleado, on_delete=CASCADE,null=True,blank=True, verbose_name="Empleado")
    type_document = models.ForeignKey(TipoDocumento, on_delete=CASCADE,null=True,blank=True, verbose_name="Tipo documento")
    name_file = models.CharField('Nombre archivo', max_length=250, null=True, blank=True)
    file = models.FileField(upload_to=upload_documentos_empleado, null=True, blank=True)
    end_date = models.DateField('Fecha de vencimiento',auto_now_add=True)
    created_at = models.DateField('Fecha de creación',auto_now_add=True)
    updated_at = models.DateField('Fecha de actualizacion', auto_now = True)
    status = models.BooleanField('Estado', default=True)


    class Meta:
        verbose_name = 'Documentos Empleado'
        verbose_name_plural = 'Documentos Empleados'

    def __str__(self):
        return "{0}".format(self.name_file)

#Con esta funcion nos aseguramos que el usuario suba la informacion requerida
def upload_documentos_empresa(instance, filename):
    return 'recursos/empresa/' + filename        

#Modelo para almacenar los documentos de la empresa
class DocumentosEmpresa(models.Model):
    empresa = models.ForeignKey(Empresa, on_delete=CASCADE,null=True,blank=True, verbose_name="Empresa inmediata")
    type_document = models.ForeignKey(TipoDocumento, on_delete=CASCADE,null=True,blank=True, verbose_name="Tipo de documento")
    name_file = models.CharField('Nombre archivo', max_length=250, null=True, blank=True)
    file = models.FileField(upload_to=upload_documentos_empresa, null=True, blank=True)
    description = models.TextField('Descripción', max_length=250, null=True, blank=True)
    created_at = models.DateField('Fecha de creación',auto_now_add=True)
    updated_at = models.DateField('Fecha de actualizacion', auto_now = True)
    status = models.BooleanField('Estado', default=True)

    class Meta:
        verbose_name = 'Documentos Empresa'
        verbose_name_plural = 'Documentos Empresas'

    def __str__(self):
        return "{0}".format(self.name_file)

#Con esta funcion nos aseguramos que el usuario suba la informacion requerida
def upload_documentos_comite(instance, filename):
    return 'recursos/comite/' + filename     


# Modelo para almacenar los documentos del comite
class DocumentosComite(models.Model):
    comite = models.ForeignKey(Comite, on_delete=CASCADE,null=True,blank=True, verbose_name="Comite")
    type_document = models.ForeignKey(TipoDocumento, on_delete=CASCADE,null=True,blank=True, verbose_name="Tipo de documento")
    file = models.FileField(upload_to=upload_documentos_comite, null=True, blank=True)
    description = models.TextField('Descripción', max_length=250, null=True, blank=True)
    created_at = models.DateField('Fecha de creación',auto_now_add=True)
    updated_at = models.DateField('Fecha de actualizacion', auto_now = True)
    status = models.BooleanField('Estado', default=True)

    class Meta:
        verbose_name = 'Documentos Comite'
        verbose_name_plural = 'Documentos Comites'

    def __str__(self):
        return "{0}".format(self.comite)






