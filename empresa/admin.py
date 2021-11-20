from django.contrib import admin

from empresa.models import *

# Register your models here.

admin.site.register(Empresa)
admin.site.register(Areas)
admin.site.register(Cargos)
admin.site.register(NivelAcademico)
admin.site.register(Empleado)
admin.site.register(Responsabilidades)
admin.site.register(TipoEmpresa)