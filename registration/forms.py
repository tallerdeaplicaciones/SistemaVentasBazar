from django import forms
from django.contrib.auth.models import AbstractUser
from registration.models import Persona

class PersonaForm(forms.ModelForm):
    
    class Meta:
        model = Persona
        fields = ['run', 'nombre', 'apellido', 'fecha_nacimiento', 'telefono', 'email']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['run'].widget = forms.TextInput(attrs={'class': 'form-control'})
        self.fields['nombre'].widget = forms.TextInput(attrs={'class': 'form-control'})
        self.fields['apellido'].widget = forms.TextInput(attrs={'class': 'form-control'})
        self.fields['fecha_nacimiento'].widget = forms.DateInput(attrs={'class': 'form-control'})
        self.fields['telefono'].widget = forms.TextInput(attrs={'class': 'form-control'})
        self.fields['email'].widget = forms.EmailInput(attrs={'class': 'form-control'})
        