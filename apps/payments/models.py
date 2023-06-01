from django.db import models
from django.contrib.auth import get_user_model
from apps.session.models import Sesion  # Import Sesion model

class Pago(models.Model):
    usuario = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    sesion = models.ForeignKey(Sesion, on_delete=models.CASCADE)
    cantidad = models.DecimalField(max_digits=6, decimal_places=2)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.usuario.username} - {self.cantidad}"