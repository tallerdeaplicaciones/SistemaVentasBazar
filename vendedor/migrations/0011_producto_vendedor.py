# Generated by Django 4.2.7 on 2023-12-23 17:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vendedor', '0010_alter_vendedor_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='vendedor',
            field=models.ForeignKey( on_delete=django.db.models.deletion.CASCADE, to='vendedor.vendedor'),
            preserve_default=False,
        ),
    ]