from django.contrib import admin
from .models import Cliente, Autor , Libro , Reserva
# Register your models here.

admin.site.register(Cliente)
admin.site.register(Autor)
admin.site.register(Libro)
admin.site.register(Reserva)