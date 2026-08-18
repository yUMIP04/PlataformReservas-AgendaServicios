from django.shortcuts import render, redirect
from django.contrib import messages
from services.models import Catalogo
from booking.models import Cita
from users.models import Usuario

# Create your views here.

#=============================================
"""================ RUTAS ================"""
#=============================================


"""🌟========================= CATALOGO 🌟========================="""
#🌟MUESTRA DE CATALOGOS PRINCIPAL

def catalogo(request):
    try:

        if request.method == 'GET':
           resultados = Catalogo.objects.all()


           return render(request, 'booking/catalogo.html', {'servicios': resultados})

        elif request.method == 'POST':
            nombre_servicio = request.POST.get('nombre_servicio', '')
            horario_inicial = request.POST.get('horario_inicial', '')
            horario_terminar = request.POST.get('horario_terminar', '')
            tiempo_consulta = request.POST.get('tiempo_consulta', '')

            if nombre_servicio and horario_inicial and horario_terminar and tiempo_consulta:
                        
                print(f"🗣️ El valor de nombre servicio es: {nombre_servicio}.")
                print(f"🗣️ El valor de horario inicial: {horario_inicial}.")
                print(f"🗣️ El valor de horario a terminar: {horario_terminar}.")
                print(f"🗣️ El valor de tiempo consulta: {tiempo_consulta}.")

                servicios = Catalogo.objects.filter(nombre_servicio = nombre_servicio, hora_inicio_trabajo=horario_inicial, hora_fin_trabajo=horario_terminar, tiempo_limite_cita=tiempo_consulta)
                        
                return render(request, 'booking/catalogo.html', {'servicios': servicios})
            

            if nombre_servicio:
            
                print(f"🗣️ El valor de nombre servicio es: {nombre_servicio}.")
                servicios = Catalogo.objects.filter(nombre_servicio = nombre_servicio)
            
                return render(request, 'booking/catalogo.html', {'servicios': servicios})

            if horario_inicial:

                print(f"🗣️ El valor de horario inicial: {horario_inicial}.")
                servicios = Catalogo.objects.filter(horario_inicio_trabajo = horario_inicial)
                            
                return render(request, 'booking/catalogo.html', {'servicios': servicios})

            if horario_terminar:
            
                print(f"🗣️ El valor de horario a terminar: {horario_terminar}.")
                servicios = Catalogo.objects.filter(horario_fin_trabajo = horario_terminar)
                                        
                return render(request, 'booking/catalogo.html', {'servicios': servicios})

            if tiempo_consulta:
            
                print(f"🗣️ El valor de tiempo consulta: {tiempo_consulta}.")
                servicios = Catalogo.objects.filter(tiempo_limite_cita = tiempo_consulta)
                                        
                return render(request, 'booking/catalogo.html', {'servicios': servicios})

    except Exception as e:
        print(f"❌ Hubo un error al mostrar la información en el Catálogo: {e}")
        
        return render(request, 'booking/catalogo.html', {'servicios': []})

#🌟FILTROS DE CATALOGO

def Citas(request):

    try:
        if request.method == 'GET':

           return redirect('catalogo')

        elif request.method == 'POST':
            id_cliente = request.session.get('usuario_id')
            print("El id_cliente recuperado es:", id_cliente)   

            resultados = Catalogo.objects.all()
            Dia_cita = request.POST.get('Dia-cita')
            Hora_cita = request.POST.get('Hora-cita')
            id_Catalogo = request.POST.get('id-catalogo')

            print("El id catalogo es:", id_Catalogo)
            resultados_hora_dia = Cita.objects.filter(fecha=Dia_cita,hora=Hora_cita).exists()

            if resultados_hora_dia:

               print("❌Ese horario ya existe, elige otro.")
               messages.error(request, "Cita no Disponible")

               return redirect('catalogo')

            else:
                Cita.objects.create(fecha=Dia_cita, hora=Hora_cita, id_catalogo_id= id_Catalogo, id_cliente_id=id_cliente)
                print("🥳Se creo una nueva cita con exito.")
                messages.success(request, "Se agendo la cita con exito")
                return redirect('catalogo')
    except Exception as e:

        print("❌Hubo un error al mostrar los filtros.")
        return redirect('catalogo')
    
"""🌟========================= RESERVAS 🌟========================="""
#🌟MUESTRA DE MIS RESERVAS

def mis_reservas(request, id_usuario):

    if request.method == 'GET':

        #🌟buscar el id usuario
        try:
            usuario_id = Usuario.objects.get(id = id_usuario)

            reservas = Cita.objects.filter( id_cliente = id_usuario)
            
            print("Aqui esta el id del usuario", usuario_id)
            if usuario_id and reservas:

             return render(request, 'booking/mis_reservas.html', {'usuario_info': usuario_id, 'reservas': reservas})
            
        except Exception as e:

            print(f"Hubo un error:{e}")
            return redirect('catalogo')

    if request.method == 'POST':

        try:

            #🌟Filtros
            print("🗣️ Mandando filtros...")

            nombre_servicio = request.POST.get('nombre-servicio', None)
            fecha_cita = request.POST.get('fecha-cita', None)
            hora_cita = request.POST.get('hora-cita', None)
                     
            print("🗣️ Nombre del Servicio: ", nombre_servicio)
            print("🗣️ Fecha de la Cita: ", fecha_cita)
            print("🗣️ Hora Cita: ", hora_cita)

            usuario_id = Usuario.objects.get(id = id_usuario) 

            if fecha_cita and nombre_servicio and hora_cita:
            
                reservas = Cita.objects.filter(fecha=fecha_cita, id_catalogo__nombre_servicio=nombre_servicio, hora=hora_cita)
            
                return render(request, 'booking/mis_reservas.html', {'usuario_info': usuario_id, 'reservas': reservas} )
            
            if fecha_cita:

                reservas = Cita.objects.filter(fecha=fecha_cita)

                return render(request, 'booking/mis_reservas.html', {'usuario_info': usuario_id, 'reservas': reservas} )

            if nombre_servicio:
            
                reservas = Cita.objects.filter(id_catalogo__nombre_servicio=nombre_servicio)
            
                return render(request, 'booking/mis_reservas.html', {'usuario_info': usuario_id, 'reservas': reservas} )

            if hora_cita:
            
                reservas = Cita.objects.filter(hora=hora_cita)
            
                return render(request, 'booking/mis_reservas.html', {'usuario_info': usuario_id, 'reservas': reservas} )

           
        except Exception as e:

            return render(request, 'booking/mis_reservas.html', {'reservas': []} )

        
    return render(request, 'booking/mis_reservas.html')

#🌟ELIMINAR RESERVA
def Eliminar_Reserva(request, id_reserva):

   
    try:

        id_usuario = request.session.get('usuario_id')
        reserva_id = Cita.objects.get(id= id_reserva)

        reserva_id.delete()

        print("🥳Se elimino la reserva de manera correcta.")

        messages.success(request, "Se elimno la reserva correctamente")
        return redirect('mis reservas', id_usuario=id_usuario)

    except Exception as e:

        print("❌Hubo un error al eliminar la reserva.")
        messages.error(request, "No se pudo Eliminar la reserva.")
        return redirect('mis reservas', id_usuario=id_usuario)


