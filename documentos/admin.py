from django.contrib import admin
from .models import *


# Modelo TipoDocumento
class TipoDocumentoAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ['id','name','created_at','updated_at','status']
    list_filter = ['name','created_at']
    list_per_page = 10


# Modelo DocumentosEmpleado
class DocumentosEmpleadoAdmin(admin.ModelAdmin):
    search_fields = ['name_file','end_date']
    list_display = ['id','type_document','name_file','end_date','created_at','updated_at','status']
    list_filter = ['type_document']
    list_per_page = 10

# Modelo DocumentosEmpresa
class DocumentosEmpresaAdmin(admin.ModelAdmin):
    search_fields = ['name_file']
    list_display = ['id','type_document','name_file','description','created_at','updated_at','status']
    list_filter = ['type_document']
    list_per_page = 10

# Modelo DocumentosComite
class DocumentosComiteAdmin(admin.ModelAdmin):
    search_fields = ['type_document']
    list_display = ['id','type_document','description', 'status']
    list_filter = ['type_document']
    list_per_page = 10


# Register your models here.

admin.site.register(TipoDocumento, TipoDocumentoAdmin)
admin.site.register(DocumentosEmpleado, DocumentosEmpleadoAdmin)
admin.site.register(DocumentosEmpresa, DocumentosEmpresaAdmin)
admin.site.register(DocumentosComite, DocumentosComiteAdmin)


