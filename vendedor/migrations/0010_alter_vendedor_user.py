# Generated by Django 4.2.7 on 2023-12-22 18:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('vendedor', '0009_alter_vendedor_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendedor',
            name='user',
            field=models.OneToOneField(to="auth.user",on_delete=django.db.models.deletion.CASCADE, ),
        ),
    ]