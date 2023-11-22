# vendedor/views.py

from django.shortcuts import render
from django.views import View

class VendedorView(View):
    template_name = 'vendedor/vendedor.html'  # Asegúrate de tener la ruta correcta al template

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
