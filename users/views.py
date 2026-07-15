from django.shortcuts import render
from .models import Usuario
# Create your views here.


def index(request):

    if request.method == 'GET':
        return render(request, 'users/index.html')

    elif request.method == 'POST':

        nombre = request.POST['nombre_usuario']
        apellido = request.POST['apellido_usuario']
        correo = request.POST['correo_usuario'] 
        clave = request.POST['password']
        clave_confirm = request.POST['password_confirm']
        rol = request.POST['rol']

        if clave_confirm == clave:

            Usuario.objects.create(nombre=nombre, apellido=apellido, correo=correo, clave=clave, rol=rol)
            print("🥳Se inserto correctamente el usuario")
        
        
    return render(request, 'users/index.html')