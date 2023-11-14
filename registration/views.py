from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import AbstractUser
from registration.forms import PersonaForm
from registration.models import Persona
from django import forms
# Create your views here.

class SignUpView(CreateView):
    form_class = PersonaForm
    template_name = 'registration/sign_up.html'

    def get_success_url(self):
        return reverse_lazy('login')

    def get_form(self, form_class=None):
        form = super(SignUpView, self).get_form()

        # Add custom widgets to form fields
        form.fields['run'].widget = forms.TextInput(attrs={'class': 'form-control'})
        form.fields['nombre'].widget = forms.TextInput(attrs={'class': 'form-control'})
        form.fields['apellido'].widget = forms.TextInput(attrs={'class': 'form-control'})
        form.fields['fecha_nacimiento'].widget = forms.DateInput(attrs={'class': 'form-control'})
        form.fields['telefono'].widget = forms.TextInput(attrs={'class': 'form-control'})
        form.fields['email'].widget = forms.EmailInput(attrs={'class': 'form-control'})

        return form
    
class ProfileUpdate(UpdateView):
    form_class = PersonaForm
    success_url = reverse_lazy('profile')
    template_name = 'registration/profile_form.html'
    
    def get_object(self):
        profile, created = Persona.objects.get_or_create(user = self.request.user)
        return profile