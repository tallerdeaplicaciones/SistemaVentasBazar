from django.db import models

# Create your models here.


class DocumentoTributario(models.Model):
    TIPO_OPCIONES = [
        ('factura', 'Factura'),
        ('boleta', 'Boleta'),
    ]
    tipo = models.CharField(max_length=10, choices=TIPO_OPCIONES)
    

class Venta(models.Model):
    documento_tributario = models.ForeignKey(DocumentoTributario, on_delete=models.CASCADE, related_name='ventas')
    fecha = models.DateField(auto_now_add=True)