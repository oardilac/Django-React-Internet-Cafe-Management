from django.contrib import admin
from .models import Pago

@admin.register(Pago)
class PagoAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'sesion', 'cantidad', 'fecha')
    search_fields = ('usuario__username', 'sesion__usuario__username')