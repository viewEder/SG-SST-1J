from django.urls import path
from django.urls.resolvers import URLPattern        # Resuelve las Rutas
from .views import ComitePageView                   # Vista donde resuelvo la ruta


urlpatterns = [
    path('comite/', ComitePageView.as_view(), name="comite"),
]
