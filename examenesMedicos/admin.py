from django.contrib import admin
from .models import*

#Modelo ActividaesPeligro
class ActividaesPeligroAdmin(admin.ModelAdmin):
    search_fields = ['area','routine']
    list_display = ['id', 'process','area','routine','description', 'status', 'created_at','updated_at']
    list_filter = ['area','routine']
    list_per_page = 10

#Modelo Clasificacion
class ClasificacionAdmin(admin.ModelAdmin):
    search_fields = ['classification_name']
    list_display = ['id', 'classification_name', 'status', 'created_at','updated_at']
    list_filter = ['classification_name']
    list_per_page = 10

#Modelo EfectoPosible
class EfectoPosibleAdmin(admin.ModelAdmin):
    search_fields = ['effects_name']
    list_display = ['id', 'effects_name', 'status', 'created_at','updated_at']
    list_filter = ['effects_name']
    list_per_page = 10

#Modelo Fuente
class FuenteAdmin(admin.ModelAdmin):
    search_fields = ['source_name']
    list_display = ['id', 'source_name', 'status', 'created_at','updated_at']
    list_filter = ['source_name']
    list_per_page = 10

#Modelo Medio
class MedioAdmin(admin.ModelAdmin):
    search_fields = ['medium_name']
    list_display = ['id', 'medium_name', 'status', 'created_at','updated_at']
    list_filter = ['medium_name']
    list_per_page = 10

#Modelo ExamenMedico
class ExamenMedicoAdmin(admin.ModelAdmin):
    search_fields = ['classification']
    list_display = ['id','activitie_danger', 'classification', 'possible_effects','source','medium','individual','deficiency_level','exposure_level','probability_level','probability_level_interpretation','consequence_level','risk_level','risk_acceptance','plant','mission','contractors','practitioners','risk_level_interpretation','worst_concecuence','legal_requirement','elimination','substitution','engineering_control','administrator_control','equipment_elements_pp','activitie_danger', 'status','created_at','updated_at']
    list_filter = ['created_at']
    list_per_page = 10


# Register your models here.
admin.site.register(ActividaesPeligro,ActividaesPeligroAdmin)
admin.site.register(ExamenMedico, ExamenMedicoAdmin)
admin.site.register(Clasificacion, ClasificacionAdmin)
admin.site.register(EfectoPosible, EfectoPosibleAdmin)
admin.site.register(Fuente, FuenteAdmin)
admin.site.register(Medio, MedioAdmin)

