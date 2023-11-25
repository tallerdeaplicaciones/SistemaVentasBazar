# Generated by Django 4.2.7 on 2023-11-25 20:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vendedor', '0001_initial'),
        ('jefeVentas', '0002_alter_productos_imagen'),
    ]

    operations = [
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Caja',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('monto', models.IntegerField()),
                ('fecha_termino', models.DateTimeField(blank=True, null=True)),
                ('estado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jefeVentas.estado')),
                ('jefeVentas', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vendedor.vendedor')),
            ],
        ),
    ]
