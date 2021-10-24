from django.shortcuts import render, get_object_or_404, redirect
from django.forms import modelform_factory

# Create your views here.

from empresa.forms import EmpresaForm
from empresa.models import Empresa

def nuevaEmpresa(request):
    if request.method == 'POST':
        formaEmpresa = EmpresaForm(request.POST)
        if formaEmpresa.is_valid():
            formaEmpresa.save()
            return redirect('index')
    else:
        formaPersona = EmpresaForm()
    return render(request, 'empresa/nuevo.html', {'formaEmpresa': formaEmpresa})

 