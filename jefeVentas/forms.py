from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    tipo_usuario = forms.ChoiceField(choices=[('jefe_ventas', 'Jefe de Ventas'), ('vendedor', 'Vendedor')])

    class Meta:
        model = User
        fields = UserCreationForm.Meta.fields + ('tipo_usuario',)
