# Generated by Django 4.2.7 on 2023-12-22 05:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jefeVentas', '0002_venta_fecha_venta_iva_venta_precio_total_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='venta',
            name='documento_tributario',
        ),
        migrations.DeleteModel(
            name='DocumentoTributario',
        ),
        migrations.DeleteModel(
            name='Venta',
        ),
    ]