from django.contrib import admin
from .models import Turno, Vendedor, Cliente, Venta, DetalleCompra, TipoDocumentoTributario, InformeDiario,Cargo
# Register your models here.

admin.site.register(Turno)

admin.site.register(Cargo)

admin.site.register(Vendedor)

admin.site.register(Cliente)

admin.site.register(Venta)

admin.site.register(DetalleCompra)

admin.site.register(TipoDocumentoTributario)

admin.site.register(InformeDiario)