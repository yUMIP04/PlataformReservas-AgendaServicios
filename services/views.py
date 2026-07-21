from django.shortcuts import render, redirect

# Create your views here.

#🌟LISTAS DE SERVICIOS

def lista_servicios(request):

    if request.method == 'GET':

        return render(request, 'services/lista_servicios.html')
    
    return render(request, 'services/lista_servicios.html')

#🌟CREACION DE SERVICIOS

def crear_servicios(request):

    if request.method == 'GET':

        return render(request, "crear_servicio.html")
        
    return render(request, "crear_servicio.html")

#🌟EDITAR DE SERVICIOS

def editar_servicios(request):

    if request.method == 'GET':

        return render(request, "editar_servicio.html")

    return render(request, "editar_servicio.html")