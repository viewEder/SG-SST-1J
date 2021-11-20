from django.contrib import admin
from .models import *

#Modelo Peligro
class PeligroAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ['id','name','created_at','updated_at', 'status']


#Modelo Accidentabilidad
class AccidentabilidadAdmin(admin.ModelAdmin):
    search_fields = ['date']
    list_display = ['id','date','inability_days','cie10','diagnosis','accident_description','accident_type','part_body_affected','accident_mechanism','accident_agent','lesion_type','basic_cause','immediate_cause','intervention_measure','compliance','empleado','peligro','status','created_at','updated_at']

# Register your models here.
admin.site.register(Peligro, PeligroAdmin)
admin.site.register(Accidentabilidad, AccidentabilidadAdmin)
