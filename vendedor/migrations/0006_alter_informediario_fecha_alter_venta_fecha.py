# Generated by Django 4.2.7 on 2023-12-24 03:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendedor', '0005_informediario_remove_caja_monto_alter_venta_fecha_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='informediario',
            name='fecha',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='venta',
            name='fecha',
            field=models.DateField(),
        ),
    ]
