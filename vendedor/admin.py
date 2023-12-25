from django.contrib import admin
from .models import Turno, Vendedor, Cliente, Venta, DetalleCompra, TipoDocumentoTributario, InformeDiario,Cargo
# Register your models here.

class TurnoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'hora_inicio', 'hora_termino', 'descripcion']  # Muestra los campos principales
    list_filter = ['nombre', 'hora_inicio', 'hora_termino']  # Permite filtrar por diferentes criterios
    search_fields = ['nombre', 'descripcion']  # Habilita la búsqueda por nombre y descripción

admin.site.register(Turno, TurnoAdmin)
admin.site.register(Turno)

admin.site.register(Cargo)

admin.site.register(Vendedor)

admin.site.register(Cliente)

admin.site.register(Venta)

admin.site.register(DetalleCompra)

admin.site.register(TipoDocumentoTributario)

admin.site.register(InformeDiario)