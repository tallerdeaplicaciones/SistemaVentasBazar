from django.views.generic.list import ListView
from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from .models import Productos, Caja, Estado
from .forms import ProductoForm, CajaForm, CajaUpdateForm
from django.utils import timezone

# Create your views here.
class Pagina_principal(TemplateView):
    template_name = "jefeVentas/home_jefeVentas.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        vendedor_actual = self.request.user.vendedor  # Asegúrate de tener este atributo en tu usuario
        cajas = Caja.objects.filter(jefeVentas=vendedor_actual)
        caja_abierta = any(caja.estado.nombre == 'Abierto' for caja in cajas)
        context['cajas'] = cajas
        context['caja_abierta'] = caja_abierta
        return context


class Pagina_inventario(ListView):
    model = Productos
    template_name = "jefeVentas/inventario/inventario.html"
    context_object_name= 'productos'


class ProductoCreateView(CreateView):
    model= Productos
    form_class =ProductoForm
    template_name='jefeventas/inventario/formulario.html'
    success_url = reverse_lazy('pagina_inventario')


class ProductoUpdateView(UpdateView):
    model = Productos
    form_class = ProductoForm
    template_name = 'jefeVentas/inventario/edit_form.html'
    success_url = reverse_lazy('pagina_inventario')


class ProductoDeleteView(DeleteView):
    model = Productos
    template_name = 'jefeVentas/inventario/delete.html'
    success_url = reverse_lazy('pagina_inventario')


class CajaCreateView(CreateView):
    model= Caja
    form_class = CajaForm
    template_name='jefeventas/caja/crear_caja.html'
    success_url = reverse_lazy('pagina_principal')

    def form_valid(self, form):
        # Asignar el estado por defecto "Abierto" a la nueva caja
        estado_abierto = Estado.objects.get(nombre="Abierto")
        caja = form.save(commit=False)
        
        # Asignar el vendedor actual al campo jefeVentas
        vendedor_actual = self.request.user.vendedor  # Asegúrate de tener este atributo en tu usuario
        caja.jefeVentas = vendedor_actual
        
        caja.estado = estado_abierto
        caja.save()
        return super().form_valid(form)

class CajaUpdateView(UpdateView):
    model = Caja
    form_class = CajaUpdateForm
    template_name = 'jefeVentas/caja/cerrar_caja.html'
    success_url = reverse_lazy('pagina_principal')

    def form_valid(self, form):
        caja = form.save(commit=False)
        caja.estado = Estado.objects.get(nombre='Cerrado')  # Obtener el estado 'Cerrado'
        caja.fecha_termino = timezone.now()  # Asignar la fecha y hora actual al cerrar la caja
        caja.save()
        return super().form_valid(form)