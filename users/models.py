from django.db import models

# Create your models here.

class Usuario(models.Model):

    nombre = models.CharField(max_length=30, unique=True)
    apellido = models.CharField(max_length=30)
    correo = models.EmailField(max_length=20)
    clave = models.CharField(max_length=15, unique=True)
    rol = models.CharField(max_length=15)