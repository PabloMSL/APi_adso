from django.urls import path
from .views import TareasApiView

urlpatterns = [
    path('tareas/', TareasApiView.as_view(), name='Tareas'),
    path('tareas/<str:pk>/', TareasApiView.as_view(), name="put")
]