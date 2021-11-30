from django.db import models
 
# Create your models here.
class Cliente(models.Model):
    rut = models.IntegerField(primary_key=True,verbose_name="rut")
    nombre = models.CharField(max_length=50,verbose_name="nombre")
    def __str__(self):
        return self.nombreAutor

class Autor(models.Model):
    idAutor = models.IntegerField(primary_key=True,verbose_name="Id de Autor")
    nombreAutor = models.CharField(max_length=50,verbose_name="Nombre de Autor")
    def __str__(self):
        return self.nombreAutor
 
class Libro(models.Model):
    codigo = models.CharField(max_length=6, primary_key=True, verbose_name="Codigo")
    nombre = models.CharField(max_length=30, verbose_name="Nombre de Libro")
    editorial = models.CharField(max_length=20,null=True,blank=True, verbose_name="Editorial")
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre

class Reserva(models.Model):
    codigo = models.CharField(max_length=6, primary_key=True, verbose_name="Codigo")
    fechaReserva = models.DateTimeField(auto_now_add=True,blank=True)
    cliente = models.ForeignKey(Autor, on_delete=models.CASCADE)
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.libro.nombre} {self.cliente.rut} - {self.fechaReserva}" 