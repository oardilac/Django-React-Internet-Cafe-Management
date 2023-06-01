from django.contrib import admin
from .models import Sesion

@admin.register(Sesion)
class SesionAdmin(admin.ModelAdmin):
    list_display = ('usuario_email', 'usuario_first_name', 'usuario_last_name', 'hora_inicio', 'hora_fin')
    search_fields = ('usuario__email', 'usuario__first_name', 'usuario__last_name')
    
    def usuario_email(self, obj):
        return obj.usuario.email
    usuario_email.short_description = 'Email'

    def usuario_first_name(self, obj):
        return obj.usuario.first_name
    usuario_first_name.short_description = 'First Name'

    def usuario_last_name(self, obj):
        return obj.usuario.last_name
    usuario_last_name.short_description = 'Last Name'