# Generated by Django 4.2.7 on 2023-12-22 18:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('vendedor', '0007_rename_cargos_cargo_rename_nombre_cargo_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendedor',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.group'),
        ),
    ]
