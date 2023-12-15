from django.views.generic.edit import CreateView, FormView
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import Venta, DetalleCompra, Producto, DocumentoTributario, Caja, Cliente
from .forms import VentasForm, DetalleCompraForm
from django.utils import timezone
from django.urls import reverse_lazy
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.db.models import F, ExpressionWrapper, DecimalField, Sum
from decimal import Decimal

from django.http import JsonResponse
from django.template.loader import render_to_string

@method_decorator(login_required, name='dispatch')
class VendedorView(PermissionRequiredMixin,View):
    template_name = 'vendedor/vendedor.html'  # Asegúrate de tener la ruta correcta al template
    permission_required = "vendedor.permiso_vendedores"
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


@login_required
def lista_productos(request):
    # Obtener todos los productos de la base de datos
    productos = Producto.objects.all()

    # Pasar la lista de productos al contexto
    context = {'productos': productos}

    # Renderizar la plantilla con la lista de productos
    html_content = render_to_string('vendedor/lista_productos.html', context)

    # Devolver la respuesta en formato JSON
    return JsonResponse({'html': html_content})

def obtener_producto(request, producto_id):
    try:
        producto = Producto.objects.get(pk=producto_id)
        # Puedes personalizar la respuesta según tus necesidades
        data = {'producto': {'nombre': producto.nombre, 'precio': producto.precio}}
        return JsonResponse(data)
    except Producto.DoesNotExist:
        return JsonResponse({'error': 'Producto no encontrado'}, status=404)

@method_decorator(login_required, name='dispatch')
def agregar_producto_a_venta(request, producto_id):
    producto = get_object_or_404(Producto, pk=producto_id)
    ultima_venta = Venta.objects.last()

    # Crear una instancia de DetalleCompra
    detalle_compra = DetalleCompra(producto=producto, cantidad=1, precio=producto.precio, venta=ultima_venta)
    detalle_compra.save()

    # Redirigir a la vista de la venta actual
    return redirect('ventas3')  # Ajusta esto según tus URL existentes




def confirmar_venta(request):
    if request.method == 'POST':
        # Obtener datos del cuerpo de la solicitud
        data = request.POST

        # Lógica para confirmar la venta y crear instancias en las tablas Venta y DetalleCompra
        # Puedes obtener datos adicionales de la solicitud POST si es necesario.
        # Por ejemplo, si tienes más datos, puedes obtenerlos de la solicitud AJAX como data['nombre_del_campo']

        # Ejemplo de creación de instancias de Venta y DetalleCompra
        venta = Venta.objects.create(
            fecha=timezone.now(),
            subtotal=data['subtotal'],
            iva=data['iva'],
            precio_total=data['precio_total'],
            vendedor=request.user.vendedor,
            cliente = Cliente.objects.get(id=data['cliente_id']),
            caja= Caja.objects.get(nombre='Predeterminada')  # Ajusta según tu lógica
        )
        
        detalle_compra = DetalleCompra.objects.create(
            producto=Producto.objects.get(id=data['producto_id']),
            cantidad=data['cantidad'],
            precio=data['precio'],
            venta=venta
        )

        # Puedes devolver una respuesta JSON indicando el éxito o cualquier información adicional.
        return JsonResponse({'mensaje': 'Venta confirmada con éxito'})

    # Devuelve una respuesta de error si la solicitud no es POST
    return JsonResponse({'error': 'Método no permitido'}, status=405)
