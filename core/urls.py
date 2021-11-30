
from django.urls import path
from .views import home,galeria,nosotros,formulario
urlpatterns = [
    path('',home, name="home"),
    path('galeria/',galeria, name="galeria"),
    path('nosotros/',nosotros, name="nosotros"),   
    path('formulario/',formulario, name="formulario")      
]