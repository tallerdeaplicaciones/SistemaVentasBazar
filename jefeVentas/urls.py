from django.urls import path
from .views import Pagina_principal,Pagina_inventario
from .views import ProductoCreateView,ProductoDeleteView,ProductoUpdateView, CajaCreateView,CajaUpdateView
urlpatterns = [
    path('', Pagina_principal.as_view(), name='pagina_principal'),
    path('inventario',Pagina_inventario.as_view(), name= 'pagina_inventario'),
    path('form', ProductoCreateView.as_view(), name= 'producto_crear'),
    path('update/<int:pk>/', ProductoUpdateView.as_view(), name='producto_update'),
    path('delete/<int:pk>/', ProductoDeleteView.as_view(), name='producto_delete'),
    path('caja/crear', CajaCreateView.as_view(), name='crear_caja'),
    path('caja/editar/<int:pk>/', CajaUpdateView.as_view(), name='cerrar_caja'),
]