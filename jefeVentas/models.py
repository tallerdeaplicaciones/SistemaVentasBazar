from django.db import models
from django.contrib.auth.models import User

# Create your models hecre.
class JefeVentas(models.Model):
    name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200, default=None)
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return f'{self.name} {self.last_name}'