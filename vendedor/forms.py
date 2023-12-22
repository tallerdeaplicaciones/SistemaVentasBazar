from django import forms
from .models import Vendedor, Venta, DetalleCompra
from django.forms.models import inlineformset_factory
from django.contrib.auth.models import Group, AbstractUser,User

class VendedorForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name', 'email', 'is_staff', 'is_active', 'date_joined']
        widgets = {
            'username': forms.TextInput(attrs={'class':'form-control'}),
            'first_name' : forms.TextInput(attrs={'class':'form-control'}),
            'last_name': forms.TextInput(attrs={'class':'form-control'}),
            'email' : forms.EmailInput(attrs={'class':'form-control'}),
            'is_staff' : forms.CheckboxInput(attrs={'class':'form-check-input'}),
            'is_active' : forms.CheckboxInput(attrs={'class':'form-check-input'}),
            'date_joined' : forms.DateTimeInput(attrs={'class':'form-control'})
        }


class VentasForm(forms.ModelForm):
    class Meta:
        model = Venta
        fields = ['cliente']
        widgets = {
            'fecha': forms.DateInput(attrs={'class':'form-control'}),
            'cliente': forms.Select(attrs={'class':'form-control'}),
        }


# DetalleCompraFormSet = inlineformset_factory(
#     Venta, DetalleCompra, fields=('producto', 'cantidad'), extra=1
# )

class DetalleCompraForm(forms.ModelForm):
    class Meta:
        model = DetalleCompra
        fields = ['producto', 'cantidad']
        widgets = {
            'producto': forms.Select(attrs={'class': 'form-control'}),
            'cantidad': forms.NumberInput(attrs={'class': 'form-control'}),
        }