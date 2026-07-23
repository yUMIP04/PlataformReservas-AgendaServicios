from django.db import models
from users.models import Usuario

# Create your models here.

class Catalogo(models.Model):
    hora_inicio_trabajo = models.TimeField()
    hora_fin_trabajo =models.TimeField()
    id_profesional =models.ForeignKey(Usuario, on_delete=models.CASCADE)
    nombre_servicio =models.CharField(max_length=30)
    descripcion =models.TextField()
    tiempo_limite_cita =models.CharField(max_length=30)