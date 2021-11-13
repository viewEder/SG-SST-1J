from django.contrib import admin
from comite.models import Comite,RolComite,ParticipantesComite
admin.site.register(Comite,RolComite,ParticipantesComite)

# Register your models here.
admin.site.register(Comite)


class Comite(admin.ModelAdmin):
    list_display=('','')
admin.site.register(RolComite)
admin.site.register(ParticipantesComite)