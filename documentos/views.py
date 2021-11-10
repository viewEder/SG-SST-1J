from django.views.generic import TemplateView
from django.shortcuts import render


# View para los documentos
class TipoDocumentoPageView(TemplateView):
    print('llega')
    template_name = 'documentos/documentos.html'
    

