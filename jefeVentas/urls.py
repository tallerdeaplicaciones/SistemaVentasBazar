from django.urls import path
from .views import Pagina_principal
urlpatterns = [
    path('', Pagina_principal.as_view(), name='pagina_principal'),
]