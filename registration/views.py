from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from vendedor.models import Vendedor
from vendedor.forms import VendedorForm
from django.contrib.auth.forms import UserCreationForm
from django import forms

#aqui estamos manejando el inicio de sesion y como 
# son direccionados los dos tipos de usuarios + un mensaje de error en caso de
# que el usuario no sea ni vendedor ni jefe

class CustomLoginView(LoginView):
    def form_valid(self, form):
        response = super().form_valid(form)
        # Lógica de redirección basada en grupos
        return grupo_usuario(self.request)

# esta funcion nos ayuda a identificar el grupo al 
# cual pertenece el usuario y hacia donde redirigirlo  
def grupo_usuario(request):
    if request.user.groups.filter(name='jefeVentas').exists():
        # Usuario pertenece al grupo 'jefedeventas'
        return redirect('pagina_principal')
    elif request.user.groups.filter(name='vendedores').exists():
        # Usuario pertenece al grupo 'vendedor'
        return redirect('vendedor')
    else:
        # Usuario no pertenece a ninguno de los grupos, manejar según tus necesidades
        return render(request, 'registration/error_usuario.html')
    
# incorporamos logout personalizado para 
# volver a la vista de login cuando hacemos logout   
class CustomLogoutView(LogoutView):
    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        return redirect('login')


class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/sign_up.html'
    
    def get_success_url(self):
        return reverse_lazy('profile')
    
    def get_form(self, form_class=None):
        form = super(SignUpView, self).get_form()

        form.fields['username'].widget = forms.TextInput(attrs={'class': 'form-control'})
        form.fields['password1'].widget = forms.PasswordInput(attrs={'class': 'form-control'})
        form.fields['password2'].widget = forms.PasswordInput(attrs={'class': 'form-control'})

        return form
    # def form_valid(self, form):
    #     response = super().form_valid(form)
    #     user = self.object

        
    
class ProfileUpdate(UpdateView):
    form_class = VendedorForm
    success_url = reverse_lazy('pagina_principal')
    template_name = 'registration/profile_form.html'
    
    def get_object(self):
        profile, created = Vendedor.objects.get_or_create(user=self.request.user)
        return profile

    def form_valid(self, form):
        print(form.cleaned_data)  # Imprime los datos del formulario
        return super().form_valid(form)
    
        



