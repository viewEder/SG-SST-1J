from django.db import models
from django.db.models.deletion import CASCADE
from empresa.models import TipoEmpresa

# Create your models here.

class Proveedor(models.Model):
    tipo_empresa = models.ForeignKey(TipoEmpresa, on_delete=CASCADE)
    razon_social = models.CharField(verbose_name="Razon Social", max_length=255, null=False,blank=False)
    nit = models.CharField(verbose_name="Nit", max_length=30, null=False,blank=False,unique=True)
    certificador_arl = models.CharField(verbose_name="Certificado ARL", max_length=255)
    es_autorizado = models.BooleanField(verbose_name="Es Autorizado")
    seguridad_social = models.CharField(verbose_name="Seguridad Social", max_length=30)
    ficha_seg_productos = models.CharField(verbose_name="Ficha Productos", max_length=255)
    telefono1 = models.CharField(verbose_name="Telefono 1", max_length=30)
    telefono2 = models.CharField(verbose_name="Telefono 2", max_length=30)
    email = models.EmailField(verbose_name="Email")
    activo = models.BooleanField(verbose_name="Activo",default=True)
    create_at = models.DateField(auto_now_add=True, verbose_name="Creado el", null=True)  
    modify_at = models.DateField(auto_now=True, verbose_name="Actualizado el")

    class Meta:
        verbose_name = 'Proveedor'
        verbose_name_plural = 'Proveedores'
    
    def __str__(self):
        return f(self.razon_social)


#Con esta funcion nos aseguramos que el usuario suba la informacion requerida
def custom_upload_to(instance, filename):
    old_instance = Elementos_PP.objects.get(pk=instance.pk)
    old_instance.avatar.delete()
    return 'epp/' + filename

class Elementos_PP(models.Model):
    nombre = models.CharField(verbose_name="Nombre EPP",max_length=255, null=False,blank=False)
    imagen = models.ImageField(upload_to=custom_upload_to, null=True, blank=True)
    activo = models.BooleanField(verbose_name="Activo",default=True)
    create_at = models.DateField(auto_now_add=True, verbose_name="Creado el", null=True)  
    modify_at = models.DateField(auto_now=True, verbose_name="Actualizado el")

    class Meta:
        verbose_name = 'Elementos de Proteccion Personal'
        verbose_name_plural = 'Elementos de Proteccion Personal'
    
    def __str__(self):
        return f(self.nombre)

class Elementos_Proveedor(models.Model):
    id_proveedor = models.ForeignKey(Proveedor, on_delete=CASCADE)
    id_elemento = models.ForeignKey(Elementos_PP, on_delete=CASCADE)
    vida_util = models.IntegerField(verbose_name="Meses de Vida Util")
    activo = models.BooleanField(verbose_name="Activo",default=True)
    create_at = models.DateField(auto_now_add=True, verbose_name="Creado el", null=True)  
    modify_at = models.DateField(auto_now=True, verbose_name="Actualizado el")

    class Meta:
        verbose_name = 'Elementos Proveedor'
        verbose_name_plural = 'Elementos Proveedor'