from django.contrib import admin
from indicadores.models import TipoIndicador,Indicadores


# Register your models here.

class IndicadoresAdmin(admin.ModelAdmin):
    
    list_display = ['nombre']   
    search_fields = ['nombre']    
    list_filter = ['nombre']

    class Meta:
        models = 'Indicadores'
admin.site.register(Indicadores,IndicadoresAdmin)

class TipoIndicadorAdmin(admin.ModelAdmin):
    
    list_display = ['tipo_indicador']   
    search_fields = ['tipo_indicador']    
    list_filter = ['tipo_indicador']

    class Meta:
        models = 'TipoIndicador'
admin.site.register(TipoIndicador,TipoIndicadorAdmin)