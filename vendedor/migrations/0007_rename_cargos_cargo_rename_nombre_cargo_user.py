# Generated by Django 4.2.7 on 2023-12-22 17:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vendedor', '0006_cargos_alter_informediario_fecha_alter_venta_fecha'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Cargos',
            new_name='Cargo',
        ),
        migrations.RenameField(
            model_name='cargo',
            old_name='nombre',
            new_name='user',
        ),
    ]
