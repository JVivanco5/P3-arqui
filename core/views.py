from .models import Libro
from django.shortcuts import render

# Create your views here.
def home(request):
   return render(request, "index.html" )
def galeria(request):
    return render(request, "galeria.html" )
def formulario(request):
    libros=Libro.objects.all()
    contexto={ 
        "libros":libros
    }
    return render(request, "formulario.html",contexto )    
def nosotros(request):
    return render(request, "nosotros.html" )


