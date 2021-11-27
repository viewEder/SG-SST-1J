from django.contrib import admin
from .models import Plan_Capacitacion, Capacitaciones

# Register your models here.

class CapacitacionAdmin(admin.ModelAdmin):
    list_display_list = ('tema','area','responsable')
    search_fields = ('tema',)
    list_filter = ('tema',)
    readonly_fields = ('create_at','modify_at')

    class Meta:
        model = Capacitaciones

class PlanCapacitacionAdmin(admin.ModelAdmin):
    readonly_fields = ('create_at','modify_at')
    list_display_list = ('periodo','objetivo',)
    search_fields = ('objetivo','justificacion')
    list_filter = ('objetivo',)

    class Meta:
        model = Plan_Capacitacion
    
admin.site.register(Plan_Capacitacion,PlanCapacitacionAdmin)
admin.site.register(Capacitaciones,CapacitacionAdmin)