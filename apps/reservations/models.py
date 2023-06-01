from django.db import models

class Tarifa(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True)
    costo_por_hora = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.nombre
