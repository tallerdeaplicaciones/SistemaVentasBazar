from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import JefeVentas

class JefeVentasForm(forms.ModelForm):
    class Meta:
        model = JefeVentas
        fields = ['name', 'last_name', 'user']
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'last_name': forms.TextInput(attrs={'class':'form-control'}),
            'user': forms.Select(attrs={'class':'form-control'})
        }
        

