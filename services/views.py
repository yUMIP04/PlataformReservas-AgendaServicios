from django.shortcuts import render, redirect

# Create your views here.

def lista_servicios(request):

    if request.method == 'GET':

        return redirect(request, 'services/lista_servicios.html')
    
    return render(request, 'services/lista_servicios.html')