from django.urls import path
from . import views

urlpatterns = [
    path('registro/', views.index, name='registro'),
    path('Inicio/', views.Inicio, name='Inicio'),
]
