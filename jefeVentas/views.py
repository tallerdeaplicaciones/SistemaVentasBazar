from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
class Pagina_principal(TemplateView):
    template_name = "jefeVentasT/home_jefeVentas.html"
