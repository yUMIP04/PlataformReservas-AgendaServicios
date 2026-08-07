from django.shortcuts import render, redirect
from .models import Catalogo

# Create your views here.

#🌟LISTAS DE SERVICIOS

def lista_servicios(request):

    if request.method == 'GET':

        usuario_id = request.session.get('usuario_id')

        resultados = Catalogo.objects.filter(id_profesional = usuario_id)
        

        return render(request, 'services/lista_servicios.html', {'servicios': resultados})
    
    return render(request, 'services/lista_servicios.html')

#🌟CREACION DE SERVICIOS

def crear_servicios(request):

    if request.method == 'GET':

        return render(request, "services/crear_servicio.html")

    elif request.method == 'POST':

        
        name_service =request.POST.get('name_service')
        descrip_service =request.POST.get('descrip_service')
        horaInicio_service =request.POST.get('horaInicio_service')
        horaFin_service =request.POST.get('horaFin_service')
        tiempoLimite_cita =request.POST.get('tiempoLimite_service')
        subir_img = request.FILES.get('subir-imagen')
        usuario_id = request.session.get('usuario_id')

        Catalogo.objects.create(hora_inicio_trabajo=horaInicio_service, hora_fin_trabajo=horaFin_service, id_profesional_id=usuario_id, nombre_servicio=name_service, descripcion=descrip_service, tiempo_limite_cita=tiempoLimite_cita, fondo_img=subir_img)

        print("🥳Se guardo el servicio correctamente.")
        return redirect('ListaServicios')
            
    return render(request, "services/crear_servicio.html")

#🌟EDITAR DE SERVICIOS

def editar_servicios(request, id_service):

    if request.method == 'GET':

        servicio = Catalogo.objects.get(id = id_service)

        return render(request, "services/editar_servicio.html", {'servicio': servicio})

    elif request.method == 'POST':

         name_service =request.POST.get('name_service')
         descrip_service =request.POST.get('descrip_service')
         horaInicio_service =request.POST.get('horaInicio_service')
         horaFin_service =request.POST.get('horaFin_service')
         tiempoLimite_cita =request.POST.get('tiempoLimite_service')
         subir_img = request.FILES.get('subir-imagen')

         actualizacion = Catalogo.objects.get(id = id_service)

         actualizacion.nombre_servicio = name_service
         actualizacion.descripcion = descrip_service
         actualizacion.hora_inicio_trabajo = horaInicio_service
         actualizacion.hora_fin_trabajo = horaFin_service
         actualizacion.tiempo_limite_cita = tiempoLimite_cita

         if subir_img :
                      actualizacion.fondo_img = subir_img

         actualizacion.save()
         return redirect('ListaServicios')

    return render(request, "services/editar_servicio.html")

#🌟ELIMINAR SERVICIO

def Eliminar_servicio(request, id_Service):

     try:

          if request.method == 'GET':

               return redirect("ListaServicios")       

          elif request.method == 'POST':
               
             eliminar = Catalogo.objects.get(id=id_Service)

             eliminar.delete()

             print("🥳 Se elimino correctamente el servicio.")

             return redirect("ListaServicios")

     except Exception as e:

          print(f"❌Hubo un error al eliminar el servicio: {e}.")

     return render(request, 'services/lista_servicios.html')