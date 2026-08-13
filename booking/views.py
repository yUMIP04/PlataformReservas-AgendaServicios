from django.shortcuts import render, redirect
from django.contrib import messages
from services.models import Catalogo
from booking.models import Cita
from users.models import Usuario

# Create your views here.

"""================ RUTAS ================"""

#🌟MUESTRA DE CATALOGOS PRINCIPAL


def catalogo(request):
    try:

        if request.method == 'GET':
           resultados = Catalogo.objects.all()


           return render(request, 'booking/catalogo.html', {'servicios': resultados})

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

               return render(request, 'booking/catalogo.html', {'servicios':resultados})

           else:
               Cita.objects.create(fecha=Dia_cita, hora=Hora_cita, id_catalogo_id= id_Catalogo, id_cliente_id=id_cliente)
               print("🥳Se creo una nueva cita con exito.")
               messages.success(request, "Se agendo la cita con exito")
               return redirect('catalogo')
        
    except Exception as e:
        print(f"❌ Hubo un error al mostrar la información en el Catálogo: {e}")
        
        return render(request, 'booking/catalogo.html', {'servicios': []})

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

        
    return render(request, 'booking/mis_reservas.html')


#🌟AREA PARA RESERVAR

def reservar(request):

    if request.method == 'GET':
        return render(request, 'booking/reservar.html')
    
    return render(request, 'booking/reservar.html')