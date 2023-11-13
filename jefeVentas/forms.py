from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'last_name', 'user']
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'last_name': forms.TextInput(attrs={'class':'form-control'}),
            'user': forms.Select(attrs={'class':'form-control'})
        }
