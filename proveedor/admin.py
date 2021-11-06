from django.contrib import admin
from .models import Proveedor, Elementos_PP, Elementos_Proveedor

# Register your models here.

admin.site.register(Proveedor)
admin.site.register(Elementos_PP)
admin.site.register(Elementos_Proveedor)