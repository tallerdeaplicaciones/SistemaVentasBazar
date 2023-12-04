from django.urls import path
from .views import VendedorView
from . import views



urlpatterns = [
    path('', VendedorView.as_view(), name='vendedor'),
    path('lista_productos/', views.lista_productos, name='lista_productos'),
    path('obtener_producto/<int:producto_id>/', views.obtener_producto, name='obtener_producto'),
]
