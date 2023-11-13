from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from .models import CustomUser
from .forms import CustomUserForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.decorators import login_required

@login_required
def my_profile(request):
    if request.user.is_authenticated and hasattr(request.user, 'is_jefeVentas') and request.user.is_jefeVentas:
        return redirect('home_jefeVentas')
    elif request.user.is_authenticated and hasattr(request.user, 'is_vendedor') and request.user.is_vendedor:
        return redirect('home_vendedor')
    else:
        return render(request, 'login.html')


class SignUpView(CreateView):
    form_class = UserCreationForm  # Utiliza el formulario personalizado
    template_name = 'registration/sign_up.html'
    
    def get_success_url(self):
        return reverse_lazy('login')
    
    def get_form(self, form_class=None):
        form = super(SignUpView, self).get_form(form_class)
        
        form.fields['username'].widget = forms.TextInput(attrs={'class':'form-control'})
        form.fields['password1'].widget = forms.PasswordInput(attrs={'class':'form-control'})
        form.fields['password2'].widget = forms.PasswordInput(attrs={'class':'form-control'})
        
        return form

class ProfileUpdate(UpdateView):
    form_class = CustomUserForm
    success_url = reverse_lazy('profile')
    template_name = 'registration/profile_form.html'
    
    def get_object(self):
        profile, created = CustomUser.objects.get_or_create(user = self.request.user)
        return profile