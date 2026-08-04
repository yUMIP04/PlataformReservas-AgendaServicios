from django.shortcuts import render, redirect
from services.models import Catalogo

# Create your views here.

"""================ RUTAS ================"""

#🌟MUESTRA DE CATALOGOS PRINCIPAL


def catalogo(request):
    try:
        
        resultados = Catalogo.objects.all()
        return render(request, 'booking/catalogo.html', {'servicios': resultados})
        
    except Exception as e:
        print(f"❌ Hubo un error al mostrar la información en el Catálogo: {e}")
        
        return render(request, 'booking/catalogo.html', {'servicios': []})


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