from django.urls import path
from .views import VendedorView 

urlpatterns = [
    path('', VendedorView.as_view(), name='vendedor'),
]
