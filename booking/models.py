from django.db import models
from users.models import Usuario
from services.models import Catalogo

# Create your models here.
class Cita(models.Model):
    fecha = models.DateField()
    hora =models.TimeField()
    id_cliente =models.ForeignKey(Usuario, on_delete=models.CASCADE)
    id_catalogo = models.ForeignKey(Catalogo, on_delete=models.CASCADE)