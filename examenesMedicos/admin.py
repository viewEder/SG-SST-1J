from django.contrib import admin
from .models import*

#Modelo ActividaesPeligro
class ActividaesPeligroAdmin(admin.ModelAdmin):
    search_fields = ['area','routine']
    list_display = ['id', 'process','area','routine','description', 'status', 'created_at','updated_at']


#Modelo ExamenMedico
class ExamenMedicoAdmin(admin.ModelAdmin):
    search_fields = ['classification']
    list_display = ['id','classification', 'sub_classification', 'effects','font','middle','individual','nd','ne','np','inp','nc','n_risk','a_risk','plant','mission','contractors','practitioners','inr','worst_concecuence','e_requirement','elimination','substitution','c_ingenierie','c_admin','equipment_elements_pp','activitie_danger', 'status','created_at','updated_at']


# Register your models here.
admin.site.register(ActividaesPeligro,ActividaesPeligroAdmin)
admin.site.register(ExamenMedico, ExamenMedicoAdmin)

