from django.db import models
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
    imagen = models.ImageField(upload_to='product_img',default='default_imagen.png')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre