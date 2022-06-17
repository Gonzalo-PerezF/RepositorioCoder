from django.db import models

# Create your models here.
class Curso(models.Model):
    nombre=models.CharField(max_length=40)  #con CharField se tiene que detallar el maximo, pongo números razonables
    comision=models.IntegerField()

class Estudiante(models.Model):
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    email= models.EmailField()

class Profesor(models.Model):
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    email= models.EmailField()
    profesion= models.CharField(max_length=30)

class Entregable(models.Model):
    nombre= models.CharField(max_length=30)
    fechaDeEntrega = models.DateField()  #sobre una fecha: dia-mes-año
    entregado = models.BooleanField()  #Trae un T o F

    class Familia(models.Model):
      name = models.CharField(max_length=20)
      surname = (models.CharField(max_length=20))
      parentezco = models.CharField(max_length=10)
      edad = models.FloatField(max_length=4)
      DNI = models.FloatField(max_length=8)
      active = models.BooleanField(default=True)

