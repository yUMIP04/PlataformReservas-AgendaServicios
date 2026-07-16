from django.urls import path
from . import views

urlpatterns = [
    path('registro/', views.index, name='registro'),
    path('Inicio/', views.Inicio, name='Inicio'),
    path('inicio_sesion/', views.inicio_sesion, name='inicio_sesion')
]
