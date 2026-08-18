from django.urls import path
from . import views

urlpatterns = [
    path('catalogo/', views.catalogo, name='catalogo'),
    path('Cita/', views.Citas, name='citas'),
    path('mis_reservas/<int:id_usuario>/', views.mis_reservas, name='mis reservas'),
    path("Eliminar_Reserva/<int:id_reserva>/", views.Eliminar_Reserva, name="Eliminar Reserva")
]