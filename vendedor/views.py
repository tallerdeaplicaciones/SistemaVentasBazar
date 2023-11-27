# vendedor/views.py
from django.views.generic.edit import CreateView, FormView
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import Venta, DetalleCompra, Producto, TipoDocumentoTributario, DocumentoTributario
from .forms import VentasForm, DetalleCompraForm
from django.utils import timezone
from django.urls import reverse_lazy
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.http import HttpResponse

class VendedorView(PermissionRequiredMixin,View):
    template_name = 'vendedor/vendedor.html'  # Asegúrate de tener la ruta correcta al template
    permission_required = "vendedor.permiso_vendedores"
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


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
        
        # Obtener la última caja abierta del vendedor actual
        caja_abierta = self.request.user.vendedor.caja_set.filter(estado__nombre='Abierto').last()
        
        if caja_abierta:
            form.instance.caja = caja_abierta
            form.instance.fecha = timezone.now().date()
            return super().form_valid(form)
        else:
            # No hay cajas abiertas, redirigir a alguna vista o mostrar un mensaje de error
            return redirect('vendedor')  
        
    def get_success_url(self):
        return reverse_lazy('ventas2')

class GenerarVenta2(PermissionRequiredMixin, FormView):
    permission_required = "vendedor.permiso_vendedores"
    template_name = 'ventas/generar_venta2.html'
    form_class = DetalleCompraForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['productos'] = Producto.objects.all()
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
        return redirect('ventas3')


class GenerarVenta3(PermissionRequiredMixin, View):
    permission_required = "vendedor.permiso_vendedores"

    def get(self, request, *args, **kwargs):
        # Obtener la última venta
        ultima_venta = Venta.objects.last()

        # Obtener todos los detalles de compra asociados a la última venta
        detalles_compra = DetalleCompra.objects.filter(venta=ultima_venta)

        # Calculando el subtotal, IVA y total
        subtotal = sum(detalle.precio for detalle in detalles_compra)
        iva = subtotal * 0.19  # Suponiendo un IVA del 19%, ajusta según tu configuración
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

        subtotal = sum(detalle.precio for detalle in detalles_compra)
        iva = subtotal * 0.19
        total = subtotal + iva

        if tipo_documento_elegido == '1':  
            vendedor = ultima_venta.vendedor  
            nuevo_documento_tributario = DocumentoTributario.objects.create(
                venta=ultima_venta,
                subtotal=subtotal,
                iva=iva,
                precio_total=total,
                tipo_id=tipo_documento_elegido,
                fecha=timezone.now().date(),
                vendedor=vendedor
            )
            # Resto del código...

            return redirect('pagina_principal')  
        
        elif tipo_documento_elegido == '2':
            vendedor = ultima_venta.vendedor  
            cliente = ultima_venta.cliente  # Obtener el cliente de la última venta
            
            nuevo_documento_tributario = DocumentoTributario.objects.create(
                venta=ultima_venta,
                subtotal=subtotal,
                iva=iva,
                precio_total=total,
                tipo_id=tipo_documento_elegido,
                fecha=timezone.now().date(),
                vendedor=vendedor,
                cliente=cliente  # Asignar el cliente al documento tributario si es factura
            )
            # Resto del código...

            return redirect('pagina_principal')  
        else:
            return HttpResponse('Tipo de documento no válido')

