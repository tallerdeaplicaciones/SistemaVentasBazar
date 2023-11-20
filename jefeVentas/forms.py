from django import forms
from .models import Productos

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Productos
        fields = ['nombre','precio', 'descripcion', 'stock','imagen','categoria']
        widgiets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'precio': forms.TextInput(attrs={'class': 'form-control'}),
            'description' : forms.TextInput(attrs={'class' : 'form-control'}),
            'stock' : forms.TextInput(attrs={'class' : 'form-control'}),
            'imagen' : forms.TextInput(attrs={'class' : 'form-control'}),
            'categoria' : forms.TextInput(attrs={'class' : 'form-control'}),
        }

