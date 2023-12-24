from django.urls import path
from .views import Pagina_principal,Pagina_inventario,Pagina_caja,Pagina_informe_diario
from .views import CajaDetailView,Error403
from .views import ProductoCreateView,ProductoDeleteView,ProductoUpdateView, ProductoDetailView,CajaCreateView,CajaUpdateView
urlpatterns = [
    path('', Pagina_principal.as_view(), name='pagina_principal'),
    path('inventario',Pagina_inventario.as_view(), name= 'pagina_inventario'),
    path('form', ProductoCreateView.as_view(), name= 'producto_crear'),
    path('update/<int:pk>/', ProductoUpdateView.as_view(), name='producto_update'),
    path('delete/<int:pk>/', ProductoDeleteView.as_view(), name='producto_delete'),
    path('detail/<int:pk>/', ProductoDetailView.as_view(), name='producto_detail'),
    path('caja/crear', CajaCreateView.as_view(), name='crear_caja'),
    path('caja/editar/<int:pk>/', CajaUpdateView.as_view(), name='actualizar_estado_caja'),
    path('caja/', Pagina_caja.as_view(), name='pagina_caja'),
    path('caja/detail/<int:pk>/', CajaDetailView.as_view(), name='pagina_caja_detail'),
    path('informeDiario/',Pagina_informe_diario.as_view(), name='informe_diario'),
    path('error', Error403.as_view(), name='error403')
]