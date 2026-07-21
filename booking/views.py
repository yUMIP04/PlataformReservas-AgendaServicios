from django.shortcuts import render, redirect
from .models import Catalogo

# Create your views here.

"""================ RUTAS ================"""

#🌟MUESTRA DE CATALOGOS PRINCIPAL

def catalogo(request):

    if request.method == 'GET':
        return render(request, 'booking/catalogo.html')
        
    return render(request, 'booking/catalogo.html')


#🌟MUESTRA DE MIS RESERVAS

def mis_reservas(request):

    if request.method == 'GET':
        return render(request, 'booking/mis_reservas.html')
    
    return render(request, 'booking/mis_reservas.html')


#🌟AREA PARA RESERVAR

def reservar(request):

    if request.method == 'GET':
        return render(request, 'booking/reservar.html')
    
    return render(request, 'booking/reservar.html')