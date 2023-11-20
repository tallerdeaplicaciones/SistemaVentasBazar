from django.views.generic.list import ListView
from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from .models import Productos
from .forms import ProductoForm
# Create your views here.
class Pagina_principal(TemplateView):
    template_name = "jefeVentasT/home_jefeVentas.html"

class Pagina_inventario(ListView):
    model = Productos
    template_name = "jefeVentasT/inventario/inventario.html"
    context_object_name= 'productos'
class ProductoCreateView(CreateView):
    model= Productos
    form_class =ProductoForm
    template_name='jefeventasT/inventario/formulario.html'
    success_url = reverse_lazy('pagina_inventario')
class ProductoUpdateView(UpdateView):
    model = Productos
    form_class = ProductoForm
    template_name = 'jefeVentasT/inventario/edit_form.html'
    success_url = reverse_lazy('pagina_inventario')
class ProductoDeleteView(DeleteView):
    model = Productos
    template_name = 'jefeVentasT/inventario/delete.html'
    success_url = reverse_lazy('pagina_inventario')