from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.

class Proveedor(models.Model):
    razon_social = models.CharField(verbose_name="Razon Social", null=False,blank=False)
    nit = models.CharField(verbose_name="Nit", null=False,blank=False,unique=True)
    certificador_arl = models.CharField(verbose_name="Certificado ARL")
    es_autorizado = models.BooleanField(verbose_name="Es Autorizado")
    seguridad_social = models.CharField(verbose_name="Seguridad Social")
    ficha_seg_productos = models.CharField(verbose_name="Ficha Productos")
    telefono1 = models.CharField(verbose_name="Telefono 1")
    telefono2 = models.CharField(verbose_name="Telefono 2")
    email = models.EmailField(verbose_name="Email")
    #tipo_empresa = models.CharField(verbose_name="Tipo Empresa")
    activo = models.BooleanField(verbose_name="Activo")
    create_at = models.DateField(auto_now_add=True, verbose_name="Creado el", null=True)  
    modify_at = models.DateField(auto_now=True, verbose_name="Actualizado el")

    class Meta:
        ordering = ['razon_social']
    
    def __str__(self):
        return f(self.razon_social)


#Con esta funcion nos aseguramos que el usuario suba la informacion requerida
def custom_upload_to(instance, filename):
    old_instance = Elementos_PP.objects.get(pk=instance.pk)
    old_instance.avatar.delete()
    return 'epp/' + filename

class Elementos_PP(models.Model):
    nombre = models.CharField(verbose_name="Nombre EPP", null=False,blank=False)
    imagen = models.ImageField(upload_to=custom_upload_to, null=True, blank=True)
    activo = models.BooleanField(verbose_name="Activo")
    create_at = models.DateField(auto_now_add=True, verbose_name="Creado el", null=True)  
    modify_at = models.DateField(auto_now=True, verbose_name="Actualizado el")

    class Meta:
        ordering = ['nombre']
    
    def __str__(self):
        return f(self.nombre)

class Elementos_Proveedor(models.Model):
    id_proveedor = models.ForeignKey(Proveedor, on_delete=CASCADE)
    id_elemento = models.ForeignKey(Elementos_PP, on_delete=CASCADE)
    vida_util = models.IntegerField(verbose_name="Vida Util")
    activo = models.BooleanField(verbose_name="Activo")
    create_at = models.DateField(auto_now_add=True, verbose_name="Creado el", null=True)  
    modify_at = models.DateField(auto_now=True, verbose_name="Actualizado el")

    class Meta:
        ordering = ['id_elemento']