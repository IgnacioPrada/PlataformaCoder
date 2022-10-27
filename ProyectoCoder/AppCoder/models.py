from cgi import MiniFieldStorage
from unittest.util import _MAX_LENGTH
from django.db import models
from django.forms import CharField, IntegerField

# Create your models here.
class Curso(models.Model):

    nombre = models.CharField( max_length=50)
    camada = models.IntegerField()

class Estudiante(models.Model):

    nombre = models.CharField( max_length=30)
    apellido = models.CharField( max_length=30)
    email = models.EmailField()

class Profesor(models.Model):

    nombre = models.CharField( max_length=50)
    apellido = models.CharField( max_length=50)
    email = models.EmailField()
    profesion = models.CharField( max_length=50)

class Entregable(models.Model):
    
    nombre = models.CharField(max_length=50)
    fechadeEntrega = models.DateField()
    entregado = models.BooleanField()
