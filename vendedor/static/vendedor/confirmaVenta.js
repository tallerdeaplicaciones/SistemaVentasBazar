// confirmarVenta.js
// Necesitas definir el botón de confirmar venta
let confirmarVentaBtn; 

export function mostrarConfirmacionVenta() {
    // Asigna valores a las variables antes de usarlas
    confirmarVentaBtn = document.getElementById('confirmarVentaBtn'); // Asegúrate de que el ID sea correcto

    // Tu lógica para mostrar la confirmación de venta
    // ...

    // Evento de clic para el botón de confirmar venta
    confirmarVentaBtn.addEventListener('click', function () {
        // Lógica para confirmar la venta
        // Por ejemplo, podrías hacer una solicitud al servidor para registrar la venta
        fetch('/vendedor/confirmar_venta/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                // Datos relacionados con la venta, si es necesario
            }),
        })
        .then(response => response.json())
        .then(data => {
            // Aquí puedes manejar la respuesta del servidor después de confirmar la venta
            console.log('Confirmación de venta exitosa:', data);
            // Puedes realizar acciones adicionales o redirigir al usuario, según tus necesidades
        })
        .catch(error => console.error('Error al confirmar la venta:', error));
    });
}


// En confirmarVenta.js
fetch('/ruta/confirmar_venta/', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/x-www-form-urlencoded',  // Ajusta según tu configuración
        // Puedes agregar encabezados adicionales si es necesario
    },
    body: new URLSearchParams({
        // Datos relacionados con la venta que estás enviando al servidor
        // Asegúrate de que coincidan con los nombres de los campos esperados en la vista de Django
        'subtotal': 'valor_subtotal',
        'iva': 'valor_iva',
        'precio_total': 'valor_precio_total',
        'cliente_id': 'valor_cliente_id',
        'producto_id': 'valor_producto_id',
        'cantidad': 'valor_cantidad',
        'precio': 'valor_precio',
    }),
})
.then(response => response.json())
.then(data => {
    // Manejar la respuesta del servidor
    console.log('Respuesta del servidor:', data);
})
.catch(error => console.error('Error al confirmar la venta:', error));
