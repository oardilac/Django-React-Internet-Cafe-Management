from django.core.validators import MinValueValidator
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Tarifa(models.Model):
    """Model to represent the rate for a session."""
    nombre = models.CharField(max_length=255)
    costo_por_hora = models.DecimalField(max_digits=5, decimal_places=2, validators=[MinValueValidator(0)])

    def __str__(self):
        return self.nombre


class ComputerSession(models.Model):
    """Model to represent a computer session."""
    nombre = models.CharField(max_length=255, unique=True)
    descripcion = models.TextField(blank=True)
    en_uso = models.BooleanField(default=False)

    def __str__(self):
        return self.nombre


class Sesion(models.Model):
    """Model to represent a user's session."""
    computadora = models.ForeignKey(ComputerSession, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)  # Use User here
    tarifa = models.ForeignKey(Tarifa, on_delete=models.CASCADE)
    hora_inicio = models.DateTimeField(auto_now_add=True)
    hora_fin = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.usuario.email} - {self.computadora.nombre}"
