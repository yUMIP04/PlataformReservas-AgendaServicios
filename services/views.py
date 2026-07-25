from django.shortcuts import render, redirect
from .models import Catalogo

# Create your views here.

#🌟LISTAS DE SERVICIOS

def lista_servicios(request):

    if request.method == 'GET':

        return render(request, 'services/lista_servicios.html')
    
    return render(request, 'services/lista_servicios.html')

#🌟CREACION DE SERVICIOS

def crear_servicios(request):

    if request.method == 'GET':

        return render(request, "services/crear_servicio.html")

    elif request.method == 'POST':

        try:
            name_service =request.POST['name_service']
            descrip_service =request.POST['descrip_service']
            horaInicio_service =request.POST['horaInicio_service']
            horaFin_service =request.POST['horaFin_service']
            tiempoLimite_cita =request.POST['tiempoLimite_service']

            usuario_id = request.session.get('usuario_id')

            Catalogo.objects.create(hora_inicio_trabajo=horaInicio_service, hora_fin_trabajo=horaFin_service, id_profesional_id=usuario_id, nombre_servicio=name_service, descripcion=descrip_service, tiempo_limite_cita=tiempoLimite_cita)

            print("🥳Se guardo el servicio correctamente.")
            return render(request, "services/crear_servicio.html" )
        except Exception as e:

            print(f"❌Hubo un error al guardar el servicio en la BD : {e}.")

    return render(request, "services/crear_servicio.html")

#🌟EDITAR DE SERVICIOS

def editar_servicios(request):

    if request.method == 'GET':

        return render(request, "editar_servicio.html")

    return render(request, "editar_servicio.html")