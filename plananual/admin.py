
from django.contrib import admin
from plananual.models import PlanAnual,EstructuraPlanAnual,EquipoResponsable,ActividadesPlan,CumplimientoPlanAnual

# Register your models here.
admin.site.register(PlanAnual)
admin.site.register(EstructuraPlanAnual)
admin.site.register(EquipoResponsable)
admin.site.register(ActividadesPlan)
admin.site.register(CumplimientoPlanAnual)