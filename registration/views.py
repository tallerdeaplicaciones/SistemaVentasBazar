from typing import Any
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.views import LoginView
from django.db import models
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django import forms
from vendedor.forms import VendedorForm
from vendedor.models import Vendedor

class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/sign_up.html'
    
    def get_success_url(self):
        return reverse_lazy('login')
    
    def get_form(self, form_class=None):
        form = super(SignUpView, self).get_form()

        form.fields['username'].widget = forms.TextInput(attrs={'class': 'form-control'})
        form.fields['password1'].widget = forms.PasswordInput(attrs={'class': 'form-control'})
        form.fields['password2'].widget = forms.PasswordInput(attrs={'class': 'form-control'})

        return form
    

class ProfileUpdate(UpdateView):
    form_class = VendedorForm
    success_url = reverse_lazy('profile')
    template_name = 'registration/profile_form.html'
    
    def get_object(self):
        profile, create = Vendedor.objects.get_or_create(user = self.request.user)
        return profile