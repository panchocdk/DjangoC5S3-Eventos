from django.db import models

# Create your models here.

#Modelo de Empleado
class Empleado(models.Model):

    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    numero_legajo = models.IntegerField()
    activo = models.BooleanField(default=True)

    def __str__(self):
        return str(self.nombre+' '+self.apellido)
    
#Modelo de Coordinador
class Coordinador(models.Model):

    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    numero_documento = models.IntegerField()
    fecha_alta = models.DateTimeField()
    activo = models.BooleanField(default=True)

    def __str__(self):
        return str(self.nombre+' '+self.apellido)
    
#Modelo de Cliente
class Cliente(models.Model):

    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    activo = models.BooleanField(default=True)

    def __srt__(self):
        return str(self.nombre+' '+self.apellido)
    
#Modelo de Servicio
class Servicio(models.Model):

    nombre = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=100)
    precio = models.IntegerField()
    activo = models.BooleanField(default=True)

    def __srt__(self):
        return str(self.nombre)
    
#Modelo de Reserva de Servicio
class ReservaDeServicio(models.Model):

    fecha_creacion = models.DateTimeField()
    fecha_reserva = models.DateField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    responsable = models.ForeignKey(Coordinador, on_delete=models.CASCADE)
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE)
    precio = models.IntegerField()
    