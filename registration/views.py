from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django import forms

class SignUpView(CreateView):
    form_class = CustomUserCreationForm  # Utiliza el formulario personalizado
    template_name = 'registration/sign_up.html'
    
    def get_success_url(self):
        return reverse_lazy('login')
    
    def get_form(self, form_class=None):
        form = super(SignUpView, self).get_form(form_class)
        
        form.fields['username'].widget = forms.TextInput(attrs={'class':'form-control'})
        form.fields['password1'].widget = forms.PasswordInput(attrs={'class':'form-control'})
        form.fields['password2'].widget = forms.PasswordInput(attrs={'class':'form-control'})
        
        return form
