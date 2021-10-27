from django.urls import path
from django.urls.resolvers import URLPattern        # Resuelve las Rutas
from .views import ProfilePageView                    # Vista donde resuelvo la ruta

urlpatterns = [ 
    path('profile/', ProfilePageView.as_view(), name="profile")
 ]