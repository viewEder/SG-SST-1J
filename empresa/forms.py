from django.db.models import fields
from django.forms import ModelForm, widgets, EmailInput
from empresa.models import Empresa

class EmpresaForm(ModelForm):
    class meta:
        model = Empresa
        fields = '__all__'
        widgets = {
            'correo': widgets.EmailInput(attrs={'type':'correo'}),
            
        }
