from collections.abc import Iterable
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class CustomUser(models.Model):
    name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200, null=True)
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return f'{self.name} {self.last_name}'