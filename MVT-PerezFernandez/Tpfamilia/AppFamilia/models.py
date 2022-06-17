from django.db import models

# Create your models here.
class Familiar(models.Model):
    nom=models.CharField(max_length=20)
    ap=models.CharField(max_length=20)
    relacion=models.CharField(max_length=15)
    edad=models.IntegerField()
    nacimiento=models.DateField()