from django.urls import path
from . import views


urlpatterns = [
    path('listaServicios/', views.lista_servicios, name='ListaServicios'),
    path('crearServicios/', views.crear_servicios, name='CrearServicios'),
    path('editarServicios/<int:id_service>/', views.editar_servicios, name='EditarServicios'),
    path('EliminarServicio/<int:id_Service>/', views.Eliminar_servicio, name='EliminarServicio'),
    path('ReservasSolicitadas/', views.Reservas_Solicitadas, name='ReservasSolicitadas')
]

