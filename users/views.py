from django.shortcuts import render

# Create your views here.


def index(request):

    if request.method == 'GET':
        return render(request, 'users/index.html')

    elif request.method == 'POST':

        nombre = request.POST['']
        apellido = request.POST['']
        correo = request.POST[''] 
        clave = request.POST['']
        clave_confirm = request.POST['']
        rol = request.POST['']

    return render(request, 'users/index.html')