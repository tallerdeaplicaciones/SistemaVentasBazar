from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django import forms

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
    
class CustomLoginView(LoginView):
    form_class = AuthenticationForm
    template_name = 'registration/login.html'

    def get_form(self, form_class=None):
        form = super(CustomLoginView, self).get_form()

        form.fields['username'].widget = forms.TextInput(attrs={'class': 'form-control'})
        form.fields['password'].widget = forms.PasswordInput(attrs={'class': 'form-control'})

        return form

class ProfileView(TemplateView):
    template_name = 'registration/profile_form.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = UserChangeForm(instance=self.request.user)
        return context
    def post(self, request, *args, **kwargs):
        form = UserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            # Puedes redirigir a una página de éxito o simplemente recargar la misma página
            return self.render_to_response(self.get_context_data(form=form, success=True))
        else:
            return self.render_to_response(self.get_context_data(form=form))