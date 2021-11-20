from django.contrib import admin
from .models import *

#Modelo Peligro
class PeligroAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ['id','name','created_at','updated_at', 'status']
    list_filter =['name', 'created_at']

#Modelo tipo accidente
class TipoAccidenteAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ['id','name','created_at','updated_at', 'status']
    list_filter =['name', 'created_at']

#Modelo Parte del cuerpo afectada
class ParteDelCuerpoAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ['id','name','created_at','updated_at', 'status']
    list_filter =['name', 'created_at']

#Modelo MecanismoAccidente
class MecanismoAccidenteAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ['id','name','created_at','updated_at', 'status']
    list_filter =['name', 'created_at']

#Modelo AgenteAccidente
class AgenteAccidenteAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ['id','name','created_at','updated_at', 'status']
    list_filter =['name', 'created_at']

#Modelo TipoLeccion
class TipoLeccionAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ['id','name','created_at','updated_at', 'status']
    list_filter =['name', 'created_at']

#Modelo CausaBasica
class CausaBasicaAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ['id','name','created_at','updated_at', 'status']
    list_filter =['name', 'created_at']

#Modelo CausaInmediata
class CausaInmediataAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ['id','name','created_at','updated_at', 'status']
    list_filter =['name', 'created_at']

#Modelo Accidentabilidad
class AccidentabilidadAdmin(admin.ModelAdmin):
    search_fields = ['date']
    list_display = ['id','date','inability_days','cie10','diagnosis','accident_description','accident_type','part_body_affected','accident_mechanism','accident_agent','lesion_type','basic_cause','immediate_cause','intervention_measure','compliance','empleado','peligro','status','created_at','updated_at']
    list_filter =['date']

# Register your models here.
admin.site.register(Peligro, PeligroAdmin)
admin.site.register(TipoAccidente, TipoAccidenteAdmin)
admin.site.register(ParteDelCuerpo, ParteDelCuerpoAdmin)
admin.site.register(MecanismoAccidente, MecanismoAccidenteAdmin)
admin.site.register(AgenteAccidente, AgenteAccidenteAdmin)
admin.site.register(TipoLeccion, TipoLeccionAdmin)
admin.site.register(CausaBasica, CausaBasicaAdmin)
admin.site.register(CausaInmediata, CausaInmediataAdmin)
admin.site.register(Accidentabilidad, AccidentabilidadAdmin)
