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



