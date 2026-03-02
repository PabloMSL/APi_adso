from django.urls import path
from .views import TareasApiView
from .views_auth import RegistroAPIView, LoginApiView
from .views_perfil import PerfilImagenAPIview

urlpatterns = [
    path('auth/registro/', RegistroAPIView.as_view(), name='api_registro'),
    path('auth/login/', LoginApiView.as_view(), name='api_login'),

    
    path('tareas/', TareasApiView.as_view(), name='Tareas'),
    path('tareas/<str:pk>/', TareasApiView.as_view(), name="put"),
    
    path("perfil/foto/", PerfilImagenAPIview.as_view(), name="apiperfilfoto")
]