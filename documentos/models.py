from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import OneToOneField

#Modelo para almacenar los tipos de documentos
class TipoDocumento(models.Model):
    name = models.CharField('Nombre', max_length= 250, null=True, blank=True)
    created_at = models.DateField('Fecha de creación',auto_now_add=True)
    updated_at = models.DateField('Fecha de actualizacion',auto_add =True, auto_now = True)
    status = models.BooleanField('Estado', default=True)
    

    class Meta:
        verbose_name = 'TipoDocumento'
        verbose_name_plural = 'TipoDocumentos'

    def __str__(self):
        return self.nombre


#Modelo para almacenar documentos de los empleados
class DocumentosEmpleado(models.Model):
    #empleado = models.ForeignKey(Empleado, on_delete=CASCADE)
    type_document = models.ForeignKey(TipoDocumento, on_delete=CASCADE)
    name_file = models.CharField('Nombre archivo', max_length=250, null=True, blank=True)
    end_date = models.DateField('Fecha de vencimiento', 'Fecha de creación',auto_now_add=True)
    created_at = models.DateField('Fecha de creación',auto_now_add=True)
    updated_at = models.DateField('Fecha de actualizacion',auto_add =True, auto_now = True)
    status = models.BooleanField('Estado', default=True)


    class Meta:
        verbose_name = 'DocumentosEmpleado'
        verbose_name_plural = 'DocumentosEmpleados'

    def __str__(self):
        return "{0}".format(self.name_file)

#Modelo para almacenar los documentos de la empresa
class DocumentosEmpresa(models.Model):
    #comite_id = models.ForeignKey(Comite, on_delete=CASCADE)
    type_document = models.ForeignKey(TipoDocumento, on_delete=CASCADE)
    title = models.CharField('Titulo', max_length=100, null=True, blank=True)
    name_file = models.CharField('Nombre archivo', max_length=250, null=True, blank=True)
    description = models.CharField('Descripción', max_length=250, null=True, blank=True)
    firm = models.CharField('Firma', max_length=45, null=True, blank=True)
    end_date = models.DateField('Fecha de vencimiento', 'Fecha de creación',auto_now_add=True)
    created_at = models.DateField('Fecha de creación',auto_now_add=True)
    updated_at = models.DateField('Fecha de actualizacion',auto_add =True, auto_now = True)
    status = models.BooleanField('Estado', default=True)

    class Meta:
        verbose_name = 'DocumentosEmpresa'
        verbose_name_plural = 'DocumentosEmpresas'

    def __str__(self):
        return "{0}".format(self.title)


