from django.db.models import fields
from django.forms import ModelForm, widgets, EmailInput
from comite.models import ParticipantesComite

class ParticipantesComiteForm(ModelForm):
    class meta:
        model = ParticipantesComite
        fields = '__all__'
      