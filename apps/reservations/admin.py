from django.contrib import admin
from .models import Tarifa

@admin.register(Tarifa)
class TarifaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion', 'costo_por_hora')
    search_fields = ('nombre',)