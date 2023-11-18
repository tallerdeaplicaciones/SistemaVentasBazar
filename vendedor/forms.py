from django import forms
from .models import Vendedor

class VendedorForm(forms.ModelForm):
    class Meta:
        model = Vendedor
        fields = ['name', 'last_name', 'user']
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'last_name': forms.TextInput(attrs={'class':'form-control'}),
            'user': forms.Select(attrs={'class':'form-control'})
        }