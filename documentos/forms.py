from django import forms
from .models import *
from django.contrib.auth.models import User
from .models import ListAppointment

class TipoDocumentoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["name"].widget.attrs.update({
            'required':'',
            'class':'form-control',
            'type':'text',
            'name':'name',
            'id':'name'
        })
        self.fields["file"].widget.attrs.update({
            'required':'',
            'class':'form-control',
            'type':'file',
            'name':'file',
            'id':'file'
        })

    class Meta:
        model = TipoDocumento
        fields = ['name', 'file']
        
