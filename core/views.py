from django.shortcuts import render
from django.views.generic import TemplateView       # Importamos la clase TemplateView

# Create your views here.
class HomePageView(TemplateView):
    # Sobreescribimos el template:
    template_name = 'core\index.html'

    # Renderizamos usando el metodo get:
    def get(self, request, *args, **kargs):
        return render(request, self.template_name, {
            'titulo': 'Sistema de Gestión de Seguridad y Salud en el Trabajo',
            'mensaje': 'Python 1J',
            'boton': 'Ingresar'
        })

