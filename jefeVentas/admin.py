from django.contrib import admin
from vendedor.models import Categoria, Producto, Caja, Estado
# Register your models here.


admin.site.register(Categoria)

admin.site.register(Producto)

admin.site.register(Estado)

admin.site.register(Caja)
