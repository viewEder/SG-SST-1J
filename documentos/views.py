from django.views.generic import TemplateView
from django.shortcuts import render


# View para los documentos
class Document(TemplateView):
    template_name = 'documentos/documents.html'
    

