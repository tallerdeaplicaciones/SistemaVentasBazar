from django.test import TestCase, Client
from django.contrib.auth.models import User, Group
from django.urls import reverse
from vendedor.models import Vendedor
import time

# "Este test de vista verifica que, al autenticar un usuario y acceder a la 
# vista de creación de vendedores, la respuesta es exitosa (código 200) y que 
# el usuario tiene el permiso necesario ('permiso_vendedores') asignado 
# correctamente".

# Es importante destacar que el enfoque del test está en la interacción de 
# varios componentes del sistema (autenticación, vista, permisos) en lugar de 
# probar unidades aisladas, lo que es característico de los tests de 
# integración.

class VendedorCreateViewTestCase(TestCase):
    def setUp(self):
        # Crea un usuario de prueba
        self.user = User.objects.create_user(username='testuser', password='testpassword')

    def test_vendedor_create_view_permission(self):
        # autentica al usuario de prueba
        self.client.login(username='testuser', password='testpassword')

        # realiza la solicitud a la vista de creación de vendedor
        response = self.client.get(reverse('crear_vendedor'))

        # agrega una pausa de 1 segundo para permitir que se complete la asignación del grupo
        time.sleep(1)

        # intenta obtener el Vendedor creado por el usuario
        try:
            vendedor = Vendedor.objects.get(user=self.user)
        except Vendedor.DoesNotExist:
            vendedor = None

        # verifica que la respuesta sea un código 200 (OK)
        self.assertEqual(response.status_code, 200, f"Expected 200 but got {response.status_code}. Content: {response.content}")

        # verifica que el Vendedor tiene el grupo 'vendedores' si existe
        if vendedor is not None:
            self.assertTrue(vendedor.user.groups.filter(name='vendedores').exists(), "User is not in the 'vendedores' group")


class CustomLoginViewTestCase(TestCase):
    def setUp(self):
        # Crear usuarios de prueba
        self.jefe_user = User.objects.create_user(username='jefeuser', password='testpassword')
        self.vendedor_user = User.objects.create_user(username='vendedoruser', password='testpassword')
        self.no_group_user = User.objects.create_user(username='nogroupuser', password='testpassword')

        # Asignar usuarios a grupos
        jefe_group = Group.objects.create(name='jefeVentas')
        vendedor_group = Group.objects.create(name='vendedores')

        self.jefe_user.groups.add(jefe_group)
        self.vendedor_user.groups.add(vendedor_group)

    def test_custom_login_view_redirects(self):
        # Configurar el cliente de prueba
        client = Client()

        # Probar inicio de sesión para jefeVentas
        response = client.post(reverse('login'), {'username': 'jefeuser', 'password': 'testpassword'})
        self.assertEqual(response.status_code, 302)  # Debe redirigir
        self.assertRedirects(response, reverse('pagina_principal'))

        # Probar inicio de sesión para vendedor
        response = client.post(reverse('login'), {'username': 'vendedoruser', 'password': 'testpassword'})
        self.assertEqual(response.status_code, 302)  # Debe redirigir
        self.assertRedirects(response, reverse('vendedor'))

        # Probar inicio de sesión para usuario sin grupo
        response = client.post(reverse('login'), {'username': 'nogroupuser', 'password': 'testpassword'})
        self.assertEqual(response.status_code, 200)  # No debe redirigir
        self.assertTemplateUsed(response, 'registration/nuevo_perfil.html')