from django.contrib import admin
from ausentismos.models import *

# Register your models here.
admin.site.register(Cie10)

class IncapacidadesAdmin(admin.ModelAdmin):
    list_display = ('mes', 'origen', 'clasificacion')
admin.site.register(Incapacidades,IncapacidadesAdmin)