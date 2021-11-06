from django.urls import path
from .views import TipoDocumentoPageView 

urlpatterns = [
    path('documentos/',TipoDocumentoPageView.as_view(), name="documentos"),
]