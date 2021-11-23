from django.contrib import admin
from .models import *

#Modelo Peligro
class PeligroAdmin(admin.ModelAdmin):
    search_fields = ['danger_name']
    list_display = ['id','danger_name','created_at','updated_at', 'status']
    list_filter =['danger_name', 'created_at']

#Modelo tipo accidente
class TipoAccidenteAdmin(admin.ModelAdmin):
    search_fields = ['accident_type_name']
    list_display = ['id','accident_type_name','created_at','updated_at', 'status']
    list_filter =['accident_type_name', 'created_at']

#Modelo Parte del cuerpo afectada
class ParteDelCuerpoAdmin(admin.ModelAdmin):
    search_fields = ['body_part_name']
    list_display = ['id','body_part_name','created_at','updated_at', 'status']
    list_filter =['body_part_name', 'created_at']

#Modelo MecanismoAccidente
class MecanismoAccidenteAdmin(admin.ModelAdmin):
    search_fields = ['mechanism_name']
    list_display = ['id','mechanism_name','created_at','updated_at', 'status']
    list_filter =['mechanism_name', 'created_at']

#Modelo AgenteAccidente
class AgenteAccidenteAdmin(admin.ModelAdmin):
    search_fields = ['agent_name']
    list_display = ['id','agent_name','created_at','updated_at', 'status']
    list_filter =['agent_name', 'created_at']

#Modelo TipoLeccion
class TipoLeccionAdmin(admin.ModelAdmin):
    search_fields = ['lesson_ame']
    list_display = ['id','lesson_ame','created_at','updated_at', 'status']
    list_filter =['lesson_ame', 'created_at']

#Modelo CausaBasica
class CausaBasicaAdmin(admin.ModelAdmin):
    search_fields = ['cause_name']
    list_display = ['id','cause_name','created_at','updated_at', 'status']
    list_filter =['cause_name', 'created_at']

#Modelo CausaInmediata
class CausaInmediataAdmin(admin.ModelAdmin):
    search_fields = ['immediate_cause_name']
    list_display = ['id','immediate_cause_name','created_at','updated_at', 'status']
    list_filter =['immediate_cause_name', 'created_at']

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
