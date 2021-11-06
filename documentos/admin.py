from django.contrib import admin
from .models import *


# Modelo TipoDocumento
class TipoDocumentoAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ['id','name','created_at','updated_at','status']


# Modelo DocumentosEmpleado
class DocumentosEmpleadoAdmin(admin.ModelAdmin):
    search_fields = ['name_file','end_date']
    list_display = ['id','type_document','name_file','end_date','created_at','updated_at','status']

# Modelo DocumentosEmpresa
class DocumentosEmpresaAdmin(admin.ModelAdmin):
    search_fields = ['title', 'name_file']
    list_display = ['id','type_document','title','name_file','description','firm','end_date','created_at','updated_at','status']

# Register your models here.

admin.site.register(TipoDocumento, TipoDocumentoAdmin)
admin.site.register(DocumentosEmpleado, DocumentosEmpleadoAdmin)
admin.site.register(DocumentosEmpresa, DocumentosEmpresaAdmin)
