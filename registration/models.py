from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Persona(AbstractUser):

    run = models.CharField(max_length=12, unique=True)
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    fecha_nacimiento = models.DateField()
    telefono = models.CharField(max_length=15)
    email = models.EmailField()
    
    def __str__(self) -> str:
        return f'{self.nombre} {self.apellido}'
# related_name campos sin conflictos, nombres unicos para cada campo
Persona.groups.field.remote_field.related_name = 'persona_groups'
Persona.user_permissions.field.remote_field.related_name = 'persona_user_permissions'

