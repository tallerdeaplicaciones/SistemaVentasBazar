from django.urls import reverse_lazy
from django.views.generic import TemplateView,DetailView,ListView,CreateView,UpdateView,DeleteView
from vendedor.models import Producto, Caja, Estado, InformeDiario,Vendedor
from .forms import ProductoForm, CajaForm, CajaUpdateForm
from django.utils import timezone
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from xhtml2pdf import pisa 



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

#Vista para el invetario.
@method_decorator(login_required, name='dispatch')
class Pagina_inventario(PermissionRequiredMixin,ListView):
    model = Producto
    template_name = "jefeVentas/inventario/inventario.html"
    context_object_name= 'productos'
    permission_required = "vendedor.permiso_jefeVentas"

#Vista para las cajas
@method_decorator(login_required, name='dispatch')
class Pagina_caja(PermissionRequiredMixin,ListView):
    model = Caja
    template_name = "jefeVentas/caja/caja.html"
    context_object_name= 'cajas'
    permission_required = "vendedor.permiso_jefeVentas"

#Vista para los informes de ventas diarios.
@method_decorator(login_required, name='dispatch')
class Pagina_informe_diario(PermissionRequiredMixin,ListView):
    model = InformeDiario
    template_name = "jefeVentas/informeVentas/informe_ventas.html"
    context_object_name = 'ventas'
    permission_required = "vendedor.permiso_jefeVentas"

@method_decorator(login_required, name='dispatch')
class ProductoCreateView(PermissionRequiredMixin,CreateView):
    model= Producto
    form_class =ProductoForm
    template_name='jefeventas/inventario/formulario.html'
    success_url = reverse_lazy('pagina_inventario')
    permission_required = "vendedor.permiso_jefeVentas"

    def form_valid(self,form):
        vendedor_instance = Vendedor.object.get(user = self.request.user)
        form.instance.vendedor = vendedor_instance
        self.object = form.save()
        response = super().form_valid(form)
        return response

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

#CRUD de caja.
@method_decorator(login_required, name='dispatch')
class CajaCreateView(PermissionRequiredMixin,CreateView):
    model= Caja
    form_class = CajaForm
    template_name='jefeventas/caja/actualizar_caja.html'
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
class CajaDetailView(PermissionRequiredMixin,DetailView):
    model = Caja
    template_name = 'jefeVentas/caja/detail.html'
    context_object_name = 'cajas'
    permission_required = "vendedor.permiso_jefeVentas"
    


@method_decorator(login_required, name='dispatch')
class CajaUpdateView(PermissionRequiredMixin,UpdateView):
    permission_required = "vendedor.permiso_jefeVentas"
    model = Caja
    form_class = CajaUpdateForm
    template_name = 'jefeVentas/caja/actualizar_caja.html'
    success_url = reverse_lazy('pagina_caja')

    def form_valid(self, form):
        caja = form.save(commit=False)
        
        if caja.estado.nombre == "Abierto":
            caja.estado = Estado.objects.get(nombre='Cerrado')  # Obtener el estado 'Cerrado'
            caja.fecha_termino = timezone.now()  # Asignar la fecha y hora actual al cerrar la caja
        else :
            caja.estado = Estado.objects.get(nombre='Abierto')
            caja.fecha_termino = None
        caja.save()
        return super().form_valid(form)

class Error403(TemplateView):
    permission_required = "vendedor.permiso_jefeVentas"
    template_name = 'jefeVentas/errores/error403.html'