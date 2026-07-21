from django.urls import path
from . import views


urlpatterns = [
    path('listaServicios/', views.lista_servicios, name='ListaServicios'),
    path('crearServicios/', views.crear_servicios, name='CrearServicios'),
    path('editarServicios/', views.editar_servicios, name='EditarServicios')
]

