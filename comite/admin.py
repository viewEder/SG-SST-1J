from django.contrib import admin
from django.db import models
from comite.models import Comite,RolComite,ParticipantesComite


# Register your models here.

class ComiteAdmin(admin.ModelAdmin):
    readonly_fields = ['created_at', 'updated_at']
    list_display = ['nombcomite']   
    search_fields = ['nombcomite']    
    list_filter = ['nombcomite']

    class Meta:
        models = 'Comite'
admin.site.register(Comite,ComiteAdmin)


class RolComiteAdmin(admin.ModelAdmin):
    
    list_display = ['tipo_rol']   
    search_fields = ['tipo_rol']
    list_filter = ['tipo_rol']
admin.site.register(RolComite,RolComiteAdmin)


class ParticipantesComiteAdmin(admin.ModelAdmin):
   
    list_display = ['empleados']
    ordering = ['empleados']
    search_fields = ['empleados']    
    list_filter =[ 'empleados']
admin.site.register(ParticipantesComite,ParticipantesComiteAdmin)