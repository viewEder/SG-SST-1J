from django.db.models import fields
from .models import Profile
from django import forms
from django.forms import widgets

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('avatar', 'telefono', 'celular', 'direccion', 'profesion')
        widgets = {
            'avatar' :  forms.ClearableFileInput(attrs = {'class':'form-control mt-2'}),
            'telefono' : forms.TextInput(attrs = {'class':'form-control mt-2', 'placeholder':'Telefono'}),
            'celular' : forms.TextInput(attrs = {'class':'form-control mt-2', 'placeholder':'Celular'}),
            'direccion' : forms.TextInput(attrs = {'class':'form-control mt-2', 'placeholder':'Dirección'}),
            'profesion' : forms.TextInput(attrs = {'class':'form-control mt-2', 'placeholder':'Profesión'}),
        }

