from django.db import models

# Create your models here.

#Modelo de Empleado
class Empleado(models.Model):

    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    numero_legajo = models.IntegerField(unique=True, blank=False)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return str(self.nombre+' '+self.apellido)
    
#Modelo de Coordinador
class Coordinador(models.Model):

    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    numero_documento = models.IntegerField(unique=True, blank=False)
    fecha_alta = models.DateTimeField(auto_now_add=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return str(self.nombre+' '+self.apellido)
    
    
#Modelo de Cliente
class Cliente(models.Model):

    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return str(self.nombre+' '+self.apellido)
    
#Modelo de Servicio
class Servicio(models.Model):

    nombre = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=100)
    precio = models.IntegerField()
    activo = models.BooleanField(default=True)

    def __str__(self):
        return str(self.nombre)
    
#Modelo de Reserva de Servicio
class ReservaDeServicio(models.Model):

    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_reserva = models.DateField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    responsable = models.ForeignKey(Coordinador, on_delete=models.CASCADE)
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE)

#Modelo para Contrataciones
class Contratacion(models.Model):
    nombre_apellido = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    direccion = models.CharField(max_length=200)
    proyecto_idea = models.CharField(max_length=200)
    mensaje = models.TextField()

    def __str__(self):
        return self.nombre_apellido