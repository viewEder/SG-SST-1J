from django.urls import path
from .views import HomePageView

urlpatterns = [
    path('', HomePageView.as_view(), name='inicio')
<<<<<<< HEAD
    
]
=======
]

>>>>>>> 29ab290b9e8490962e370b5a923b54693ae53945
