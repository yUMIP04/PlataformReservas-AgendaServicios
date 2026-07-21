from django.urls import path
from . import views

urlpatterns = [
    path('catalogo/', views.catalogo, name='catalogo'),
    path('mis_reservas/', views.mis_reservas, name='mis reservas'),
    path('reservar/', views.reservar, name='reservar')
]