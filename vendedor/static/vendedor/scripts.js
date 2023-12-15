document.addEventListener('DOMContentLoaded', function () {
    // contenedor que recibe la lista de productos
    var listaProductosContainer = document.getElementById('listaProductosContainer');
    // boton para activar la lista de productos en pantalla
    var verProductosBtn = document.getElementById('verProductosBtn');
    // este es el table que esta en lista_productos.html  osea la lista en si
    var productosTable = document.getElementById('productosTable');
    // aqui es donde estamos ingresando la lista de productos seleccionados
    var listaProductosVendedor = document.getElementById('listaProductosVendedor');
    // clarmente el container que recibe el subtotal en pantalla
    var subtotalContainer = document.getElementById('subtotalContainer');
    // lo mismo para impuestos osea el iva
    var impuestosContainer = document.getElementById('impuestosContainer');
    // aqui mostramos el total
    var totalContainer = document.getElementById('totalContainer');
    // variable para rastrear si la lista de productos está abierta
    var listaAbierta = false;
    // variable para almacenar el total
    var total = 0;
    // verificar si los elementos existen antes de intentar actualizar su contenido
    if (subtotalContainer && impuestosContainer && totalContainer) {
        // Inicializar los elementos con valores iniciales
        subtotalContainer.textContent = '0.0';
        impuestosContainer.textContent = '0.0';
        totalContainer.textContent = '0.0';

    } else {
        console.error('Al menos uno de los contenedores no se encontró en el DOM.');
    }

    // agrega un event listener al nuevo elemento de clic, este es el "icono search"
    verProductosBtn.addEventListener('click', function () {
        // alternar la visibilidad del contenedor usando la variable de seguimiento
        listaAbierta = !listaAbierta;
        listaProductosContainer.hidden = !listaAbierta;

        // Si la lista está abierta, hacer una solicitud al servidor para obtener los datos
        if (listaAbierta) {
            fetch('/vendedor/lista_productos/')
                .then(response => response.json())
                .then(data => {
                    // Actualizar la interfaz con los datos recibidos
                    productosTable.innerHTML = data.html;

                    // Agregar eventos de clic a las filas seleccionables
                    var filasSeleccionables = document.querySelectorAll('.seleccionable');
                    filasSeleccionables.forEach(function (fila) {
                        fila.addEventListener('click', function () {
                            // Manejar la lógica de agregar a la nueva lista
                            var productoId = fila.getAttribute('data-producto-id');
                            agregarALista(productoId);
                        });
                    });
                })
                .catch(error => console.error('Error al cargar los datos de productos:', error));
        }
    });

    // Agrega un event listener para cerrar el contenedor si se hace clic fuera de él
    document.addEventListener('click', function (event) {
        // Verifica si el clic no fue dentro del contenedor ni en el icono de búsqueda
        if (!verProductosBtn.contains(event.target) && !listaProductosContainer.contains(event.target)) {
            // Ocultar el contenedor solo si la lista está abierta
            if (listaAbierta) {
                listaProductosContainer.hidden = true;
                listaAbierta = false;
                // console.log('Cerraste el contenedor');
            }
        }
    });
    // función para agregar a la nueva lista
    function agregarALista(productoId) {
        // obtener información del producto del servidor (puedes personalizar según tus necesidades)
        fetch(`/vendedor/obtener_producto/${productoId}/`)
            .then(response => response.json())
            .then(data => {
                console.log('Data del producto obtenida:', data);
    
                // Crear una nueva fila en la lista de productos del vendedor
                var nuevaFila = document.createElement('tr');
                nuevaFila.innerHTML = `
                    <td>${data.producto.nombre}</td>
                    <td>${data.producto.precio}</td>
                `;
                listaProductosVendedor.querySelector('tbody').appendChild(nuevaFila);
    
                // Actualizar el total
                total += data.producto.precio;
    
                // Actualizar los elementos en el DOM
                console.log('subtotalContainer antes de actualizar:', subtotalContainer);
                subtotalContainer.textContent = total.toFixed(2); // Ajustar el formato según tus necesidades
                console.log('impuestosContainer antes de actualizar:', impuestosContainer);
                var impuestos = total * 0.10;
                impuestosContainer.textContent = impuestos.toFixed(2); // Ajustar el formato según tus necesidades
                console.log('totalContainer antes de actualizar:', totalContainer);
                var totalFinal = total + impuestos;
                totalContainer.textContent = totalFinal.toFixed(2); // Ajustar el formato según tus necesidades
            })
            .catch(error => console.error('Error al obtener información del producto:', error));
    }
    
});


