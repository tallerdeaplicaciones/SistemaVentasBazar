from django.db import models
from vendedor.models import Vendedor
# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return self.nombre

class Productos(models.Model):
    nombre = models.CharField(max_length=50, null=False, blank=False)
    precio = models.IntegerField(null=False, blank=False)
    descripcion = models.TextField(null=False, blank=False)
    stock = models.IntegerField(null=False, blank=False)
    imagen = models.ImageField(null=True, blank= True,upload_to='product_img',default='default_imagen.png')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class Estado(models.Model):
    nombre = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return self.nombre   
    
class Caja(models.Model):
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    jefeVentas = models.ForeignKey(Vendedor, on_delete=models.CASCADE)
    monto = models.IntegerField(null=False, blank=False)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE, default="Abierto")
    fecha_termino = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f'Caja {self.id}'
