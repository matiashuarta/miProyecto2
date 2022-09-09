from django.db import models

# Create your models here.
class Curso(models.Model):

    nombre = models.CharField(max_length=60)
    camada = models.IntegerField()

class Estudiante(models.Model):

    nombre = models.CharField(max_length=60)
    apellido = models.CharField(max_length=60)
    correo = models.EmailField(max_length=60)

class Profesor(models.Model):
    nombre = models.CharField(max_length=60)
    apellido = models.CharField(max_length=60)
    email = models.EmailField(max_length=60)
    profesion = models.CharField(max_length=60)

class Entregable(models.Model):
    nombre = models.CharField(max_length=60)
    fechaEntrega = models.DateField()