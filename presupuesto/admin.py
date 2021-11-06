from django.contrib import admin
from presupuesto.models import *

# Register your models here.
admin.site.register(Periodo)
admin.site.register(EjecucionPresupuesto)
admin.site.register(CronogramaPresupuesto)