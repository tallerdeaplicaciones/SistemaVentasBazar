from django.urls import path, include
from .views import SignUpView, ProfileUpdate
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('', LoginView.as_view(), name='login'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('profile/', ProfileUpdate.as_view(), name='profile'),
]