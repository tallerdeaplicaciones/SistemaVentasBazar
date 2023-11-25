from django.contrib import admin
from .models import Categoria, Productos, Caja, Estado
# Register your models here.


admin.site.register(Categoria)

admin.site.register(Productos)

admin.site.register(Estado)

admin.site.register(Caja)
