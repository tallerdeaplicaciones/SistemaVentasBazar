from django.views.generic.list import ListView
from django.urls import reverse_lazy
from django.views.generic import TemplateView,DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from vendedor.models import Producto, Caja, Estado
from .forms import ProductoForm, CajaForm, CajaUpdateForm
from django.utils import timezone
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from vendedor.models import Venta
from vendedor.models import DocumentoTributario
from django.db.models import Prefetch


# Create your views here.
@method_decorator(login_required, name='dispatch')
class Pagina_principal(PermissionRequiredMixin,TemplateView):
    template_name = "jefeVentas/home_jefeVentas.html"
    permission_required = "vendedor.permiso_jefeVentas"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        vendedor_actual = self.request.user.vendedor  # Asegúrate de tener este atributo en tu usuario
        cajas = Caja.objects.filter(jefeVentas=vendedor_actual)
        caja_abierta = any(caja.estado.nombre == 'Abierto' for caja in cajas)
        context['cajas'] = cajas
        context['caja_abierta'] = caja_abierta
        return context


@method_decorator(login_required, name='dispatch')
class Pagina_inventario(PermissionRequiredMixin,ListView):
    model = Producto
    template_name = "jefeVentas/inventario/inventario.html"
    context_object_name= 'productos'
    permission_required = "vendedor.permiso_jefeVentas"


@method_decorator(login_required, name='dispatch')
class ProductoCreateView(PermissionRequiredMixin,CreateView):
    model= Producto
    form_class =ProductoForm
    template_name='jefeventas/inventario/formulario.html'
    success_url = reverse_lazy('pagina_inventario')
    permission_required = "vendedor.permiso_jefeVentas"


@method_decorator(login_required, name='dispatch')
class ProductoUpdateView(PermissionRequiredMixin,UpdateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'jefeVentas/inventario/edit_form.html'
    success_url = reverse_lazy('pagina_inventario')
    permission_required = "vendedor.permiso_jefeVentas"


@method_decorator(login_required, name='dispatch')
class ProductoDeleteView(PermissionRequiredMixin,DeleteView):
    model = Producto
    template_name = 'jefeVentas/inventario/delete.html'
    success_url = reverse_lazy('pagina_inventario')
    permission_required = "vendedor.permiso_jefeVentas"


@method_decorator(login_required, name='dispatch')
class ProductoDetailView(PermissionRequiredMixin,DetailView):
    model = Producto
    template_name = 'jefeVentas/inventario/detail.html'
    context_object_name = 'productos'
    permission_required = "vendedor.permiso_jefeVentas"


@method_decorator(login_required, name='dispatch')
class CajaCreateView(PermissionRequiredMixin,CreateView):
    model= Caja
    form_class = CajaForm
    template_name='jefeventas/caja/crear_caja.html'
    success_url = reverse_lazy('pagina_principal')
    permission_required = "vendedor.permiso_jefeVentas"

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


@method_decorator(login_required, name='dispatch')
class CajaUpdateView(PermissionRequiredMixin,UpdateView):
    permission_required = "vendedor.permiso_jefeVentas"
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
    
class InformeVentasView(ListView):
    model = Venta
    template_name = 'jefeVentas/informeVentas/informe_ventas.html'
    context_object_name = 'ventas'

    def get_queryset(self):
        
        # No es necesario usar prefetch_related si cada Venta tiene un solo DocumentoTributario.
        return Venta.objects.prefetch_related('detallecompra_set').all()
        