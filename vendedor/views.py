from django.views.generic.edit import CreateView, FormView
from django.shortcuts import render, redirect
from django.views import View
from .models import Venta, DetalleCompra, Producto, DocumentoTributario, Caja, Cliente
from .forms import VentasForm, DetalleCompraForm, ClienteForm
from django.utils import timezone
from django.urls import reverse_lazy
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.http import HttpResponse, Http404
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from decimal import Decimal

@method_decorator(login_required, name='dispatch')
class VendedorView(PermissionRequiredMixin,View):
    template_name = 'vendedor/vendedor.html' 
    permission_required = "vendedor.permiso_vendedores"
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


@method_decorator(login_required, name='dispatch')
class GenerarVenta1(PermissionRequiredMixin,CreateView):
    model = Venta
    form_class = VentasForm
    template_name = 'ventas/generar_venta1.html'
    success_url = '/ventas/generar_venta2'
    permission_required = "vendedor.permiso_vendedores"

    def form_valid(self, form):
        # Asignar el cliente seleccionado en el formulario
        cliente = form.cleaned_data['cliente']
        form.instance.cliente = cliente
        
        # Asignar el vendedor actualmente logueado
        form.instance.vendedor = self.request.user.vendedor
        
        # Obtener la caja abierta
        caja_abierta = Caja.objects.last()

        #Verificar si la caja_abierta tiene estado == "Abierto"
        if caja_abierta.estado.nombre == "Abierto":
            # Asignar la caja abierta a la venta
            form.instance.caja = caja_abierta
            form.instance.fecha = timezone.now().date()
            return super().form_valid(form)
        else:
            # No hay cajas abiertas, redirigir a alguna vista o mostrar un mensaje de error
            return redirect('vendedor')  
        
    def get_success_url(self):
        return reverse_lazy('ventas2')

class RegistrarClienteView(CreateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'ventas/cliente_form.html'
    success_url = 'ventas1'

@method_decorator(login_required, name='dispatch')
class GenerarVenta2(PermissionRequiredMixin, FormView):
    permission_required = "vendedor.permiso_vendedores"
    template_name = 'ventas/generar_venta2.html'
    form_class = DetalleCompraForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['productos'] = Producto.objects.all()
        
        # Agregar la información del detalle de compra
        ultima_venta = Venta.objects.last()
        context['detalle_compra'] = DetalleCompra.objects.filter(venta=ultima_venta)
        
        return context

    def form_valid(self, form):
        producto_id = self.request.POST.get('producto')
        cantidad = form.cleaned_data['cantidad']
        producto = Producto.objects.get(pk=producto_id)

        # Obtener o crear una nueva Venta si no existe
        ultima_venta = Venta.objects.last()
        if not ultima_venta:
            ultima_venta = Venta.objects.create()

        # Crear una instancia de DetalleCompra
        detalle_compra = DetalleCompra(producto=producto, cantidad=cantidad, precio=producto.precio, venta=ultima_venta)
        detalle_compra.save()

        # Almacenar el ID de la Venta en la sesión para su uso posterior
        self.request.session['venta_previa_id'] = ultima_venta.id

        # Redirigir a la vista para crear la venta final
        return redirect('ventas2')

# necesito crear la vista para generar la venta final

@method_decorator(login_required, name='dispatch')
class GenerarVenta3(PermissionRequiredMixin, View):
    permission_required = "vendedor.permiso_vendedores"

    def get(self, request, *args, **kwargs):
        ultima_venta = Venta.objects.last()
        detalles_compra = DetalleCompra.objects.filter(venta=ultima_venta)

        # Calcular el subtotal basado en todos los detalles de compra asociados a la venta
        subtotal = detalles_compra.aggregate(total=Sum('precio'))['total'] or Decimal(0)
        iva = subtotal * Decimal('0.19')  # Suponiendo un IVA del 19%
        total = subtotal + iva

        return render(request, 'ventas/generar_venta3.html', {
            'subtotal': subtotal,
            'iva': iva,
            'total': total,
        })

    def post(self, request, *args, **kwargs):
        tipo_documento_elegido = request.POST.get('tipo_documento')
        ultima_venta = Venta.objects.last()
        detalles_compra = DetalleCompra.objects.filter(venta=ultima_venta)

        subtotal = sum(detalle.precio * detalle.cantidad for detalle in detalles_compra)
        iva = subtotal * Decimal('0.19')  # Suponiendo un IVA del 19%
        total = subtotal + iva

        ultima_venta.subtotal = subtotal
        ultima_venta.iva = iva 
        ultima_venta.precio_total = total
        ultima_venta.save()

        if tipo_documento_elegido == '1':
            # Crear el documento tributario para Boleta
            nuevo_documento_tributario = DocumentoTributario.objects.create(
                venta=ultima_venta,
                subtotal=subtotal,
                iva=iva,
                precio_total=total,
                tipo_id=tipo_documento_elegido,
                fecha=timezone.now().date(),
                vendedor=ultima_venta.vendedor
            )

            return redirect('vendedor')
        elif tipo_documento_elegido == '2':
            # Crear el documento tributario para Factura
            cliente = ultima_venta.cliente
            nuevo_documento_tributario = DocumentoTributario.objects.create(
                venta=ultima_venta,
                subtotal=subtotal,
                iva=iva,
                precio_total=total,
                tipo_id=tipo_documento_elegido,
                fecha=timezone.now().date(),
                vendedor=ultima_venta.vendedor,
                cliente=cliente
            )

            return redirect('vendedor')
        else:
            return HttpResponse('Tipo de documento no válido')