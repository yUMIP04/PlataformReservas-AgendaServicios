from django.urls import path
from . import views

urlpatterns = [
    path('registro/', views.index, name='registro'),
    path('Inicio/', views.Inicio, name='Inicio'),
    path('inicio_sesion/', views.inicio_sesion, name='inicio_sesion'),
    path('catalogo/', views.catalogo, name='catalogo'), 
    path('cerrar_sesion/', views.cerrar_sesion, name='cerrar_sesion')
]
