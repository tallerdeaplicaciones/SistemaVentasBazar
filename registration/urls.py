from django.urls import path
from .views import VendedorCreateView

urlpatterns = [
    path('signup/', VendedorCreateView.as_view(), name='signup'),
    # path('signup/', SignUpView.as_view(), name='signup'),
    # path('profile/', ProfileUpdate.as_view(), name='profile'),
]