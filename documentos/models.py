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
    old_instance = DocumentosEmpleado.objects.get(pk=instance.pk)
    old_instance.file.delete()
    return 'recursos/empleado/' + filename

#Modelo para almacenar documentos de los empleados
class DocumentosEmpleado(models.Model):
    name_file = models.CharField('Nombre archivo', max_length=250, null=True, blank=True)
    file = models.FileField(upload_to=upload_documentos_empleado, null=True, blank=True)
    end_date = models.DateField('Fecha de vencimiento',auto_now_add=True)
    created_at = models.DateField('Fecha de creación',auto_now_add=True)
    updated_at = models.DateField('Fecha de actualizacion', auto_now = True)
    status = models.BooleanField('Estado', default=True)
    empleado = models.ForeignKey(Empleado, on_delete=CASCADE)
    type_document = models.ForeignKey(TipoDocumento, on_delete=CASCADE)


    class Meta:
        verbose_name = 'Documentos Empleado'
        verbose_name_plural = 'Documentos Empleados'

    def __str__(self):
        return "{0}".format(self.name_file)

#Con esta funcion nos aseguramos que el usuario suba la informacion requerida
def upload_documentos_empresa(instance, filename):
    old_instance = DocumentosEmpresa.objects.get(pk=instance.pk)
    old_instance.file.delete()
    return 'recursos/empresa/' + filename        

#Modelo para almacenar los documentos de la empresa
class DocumentosEmpresa(models.Model):
    name_file = models.CharField('Nombre archivo', max_length=250, null=True, blank=True)
    file = models.FileField(upload_to=upload_documentos_empresa, null=True, blank=True)
    description = models.CharField('Descripción', max_length=250, null=True, blank=True)
    created_at = models.DateField('Fecha de creación',auto_now_add=True)
    updated_at = models.DateField('Fecha de actualizacion', auto_now = True)
    status = models.BooleanField('Estado', default=True)
    empresa = models.ForeignKey(Empresa, on_delete=CASCADE)
    type_document = models.ForeignKey(TipoDocumento, on_delete=CASCADE)

    class Meta:
        verbose_name = 'Documentos Empresa'
        verbose_name_plural = 'Documentos Empresas'

    def __str__(self):
        return "{0}".format(self.title)

#Con esta funcion nos aseguramos que el usuario suba la informacion requerida
def upload_documentos_comite(instance, filename):
    old_instance = DocumentosComite.objects.get(pk=instance.pk)
    old_instance.file.delete()
    return 'recursos/comite/' + filename     


# Modelo para almacenar los documentos del comite
class DocumentosComite(models.Model):
    file = models.FileField(upload_to=upload_documentos_comite, null=True, blank=True)
    description = models.CharField('Descripción', max_length=250, null=True, blank=True)
    created_at = models.DateField('Fecha de creación',auto_now_add=True)
    updated_at = models.DateField('Fecha de actualizacion', auto_now = True)
    status = models.BooleanField('Estado', default=True)
    comite = models.ForeignKey(Comite, on_delete=CASCADE)
    type_document = models.ForeignKey(TipoDocumento, on_delete=CASCADE)

    class Meta:
        verbose_name = 'Documentos Comite'
        verbose_name_plural = 'Documentos Comites'

    def __str__(self):
        return "{0}".format(self.comite)






