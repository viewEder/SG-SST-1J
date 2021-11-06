from django.db.models import fields
from .models import Profile
from django import forms
from django.forms import widgets, ChoiceField
from django.contrib.auth.models import User

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar', 'telefono', 'celular', 'direccion', 'profesion', 'cedula', 'genero', 'fecha_nacimiento', 'estado_civil']
        widgets = {
            'avatar': forms.ClearableFileInput(attrs = {'class':'form-control mt-2'}),
            'telefono' : forms.TextInput(attrs = {'class':'form-control mt-2', 'placeholder':'Telefono'}),
            'celular' : forms.TextInput(attrs = {'class':'form-control mt-2', 'placeholder':'Celular'}),
            'direccion' : forms.TextInput(attrs = {'class':'form-control mt-2', 'placeholder':'Dirección'}),
            'profesion' : forms.TextInput(attrs = {'class':'form-control mt-2', 'placeholder':'Profesión'}),
            'cedula' : forms.TextInput(attrs = {'class':'form-control mt-2', 'placeholder':'Cedula'}),
            'genero' : forms.Select(attrs = {'class':'form-control mt-2'}),
            'fecha_nacimiento' : forms.DateInput(format=('%Y-%m-%d'),attrs = {'class':'form-control mt-2', 'type':'date'}),
            'estado_civil' : forms.Select(attrs = {'class':'form-control mt-2'}),
        }

        #forms.ChoiceField(label="Tipo de Petición", required=True, choices=pqrsf, widget=forms.Select(attrs={'class':'form-control'}))