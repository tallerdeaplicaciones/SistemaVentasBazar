// listaProductos.js

let verProductosBtn;
let listaAbierta = false;
let listaProductosContainer;
let productosTable;
let listaProductosVendedor;
let subtotalContainer;
let impuestosContainer;
let totalContainer;
let total = 0;

export function inicializarListaProductos() {

    // Asigna valores a las variables antes de usarlas
    verProductosBtn = document.getElementById('verProductosBtn');
    listaProductosContainer = document.getElementById('listaProductosContainer');
    productosTable = document.getElementById('productosTable');
    listaProductosVendedor = document.getElementById('listaProductosVendedor'); // Agrega esta línea
    subtotalContainer = document.getElementById('subtotalContainer');
    impuestosContainer = document.getElementById('impuestosContainer');
    totalContainer = document.getElementById('totalContainer');

    // Tu lógica para inicializar la lista de productos
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
}


export function agregarALista(productoId) {
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
