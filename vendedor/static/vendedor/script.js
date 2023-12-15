// script.js

import { inicializarListaProductos, agregarALista } from './listaProductos.js';
import { mostrarConfirmacionVenta } from './confirmarVenta.js';

document.addEventListener('DOMContentLoaded', function () {
    // contenedor que recibe la lista de productos
    var listaProductosContainer = document.getElementById('listaProductosContainer');
    // boton para activar la lista de productos en pantalla
    var verProductosBtn = document.getElementById('verProductosBtn');
    // este es el table que esta en lista_productos.html osea la lista en si
    var productosTable = document.getElementById('productosTable');
    // aqui es donde estamos ingresando la lista de productos seleccionados
    var listaProductosVendedor = document.getElementById('listaProductosVendedor');
    // claamente el container que recibe el subtotal en pantalla
    var subtotalContainer = document.getElementById('subtotalContainer');
    // lo mismo para impuestos osea el iva
    var impuestosContainer = document.getElementById('impuestosContainer');
    // aqui mostramos el total
    var totalContainer = document.getElementById('totalContainer');
    // variable para rastrear si la lista de productos está abierta
    var listaAbierta = false;
    // variable para almacenar el total
    var total = 0;

  

    // Inicializar los elementos con valores iniciales
    if (subtotalContainer && impuestosContainer && totalContainer) {
        subtotalContainer.textContent = '0.0';
        impuestosContainer.textContent = '0.0';
        totalContainer.textContent = '0.0';
    } else {
        console.error('Al menos uno de los contenedores no se encontró en el DOM.');
    }

    // ... (más código existente)

    // Llamadas a funciones de otros archivos
    inicializarListaProductos();
    mostrarConfirmacionVenta();
});
