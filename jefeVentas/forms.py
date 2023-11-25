from django import forms
from .models import Productos, Caja

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Productos
        fields = ['nombre','precio', 'descripcion', 'stock','imagen','categoria']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'precio': forms.TextInput(attrs={'class': 'form-control'}),
            'description' : forms.TextInput(attrs={'class' : 'form-control'}),
            'stock' : forms.TextInput(attrs={'class' : 'form-control'}),
            'imagen' : forms.ClearableFileInput(attrs={'class' : 'form-control'}),
            'categoria' : forms.TextInput(attrs={'class' : 'form-control'}),
        }

class CajaForm(forms.ModelForm):
    class Meta:
        model = Caja
        fields = ['monto']
        widgets = {
            'monto': forms.TextInput(attrs={'class': 'form-control'}),
        }

class CajaUpdateForm(forms.ModelForm):
    class Meta:
        model = Caja
        fields = []  # Eliminar todos los campos para que no sean editables manualmente
        widgets = {
            'estado': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'fecha_termino': forms.DateTimeInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
        }