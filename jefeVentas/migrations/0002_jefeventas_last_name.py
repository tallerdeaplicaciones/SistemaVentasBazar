# Generated by Django 4.2.7 on 2023-11-13 01:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jefeVentas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='jefeventas',
            name='last_name',
            field=models.CharField(default=None, max_length=200),
        ),
    ]
