// confirmarVenta.js

// Esta función se llamará cuando el vendedor presione el botón de confirmar venta
function mostrarConfirmacionVenta() {
    // Utiliza el cuadro de diálogo nativo del navegador para obtener la confirmación del vendedor
    var confirmacion = window.confirm('¿Estás seguro de confirmar la venta?');

    // Si el vendedor confirma la venta, procede con la confirmación
    if (confirmacion) {
        // Obtener datos necesarios para la confirmación (puedes ajustar según tus necesidades)
        var subtotal = subtotalContainer.textContent;
        var iva = impuestosContainer.textContent;
        var precioTotal = totalContainer.textContent;
        var clienteId = obtenerClienteId();  // Implementa tu lógica para obtener el ID del cliente
        var productoId = obtenerProductoId();  // Implementa tu lógica para obtener el ID del producto
        var cantidad = obtenerCantidad();  // Implementa tu lógica para obtener la cantidad

        // Realiza la solicitud AJAX para confirmar la venta
        fetch('/ruta/de/confirmar_venta/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': obtenerCSRFToken(),  // Implementa tu lógica para obtener el token CSRF
            },
            body: JSON.stringify({
                subtotal: subtotal,
                iva: iva,
                precio_total: precioTotal,
                cliente_id: clienteId,
                producto_id: productoId,
                cantidad: cantidad,
            }),
        })
        .then(response => response.json())
        .then(data => {
            // Maneja la respuesta del servidor (puedes mostrar un mensaje de éxito, etc.)
            console.log('Respuesta del servidor:', data);
        })
        .catch(error => console.error('Error al confirmar la venta:', error));
    } else {
        // Puedes realizar acciones adicionales si el vendedor cancela la venta
        console.log('Venta cancelada por el vendedor');
    }
}

