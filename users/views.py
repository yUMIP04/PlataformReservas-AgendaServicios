from django.shortcuts import render, redirect
from .models import Usuario
# Create your views here.

"""=================== RUTAS ==================="""

#🌟PAGINA REGISTRO

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
            return redirect('Inicio')
        
        
    return render(request, 'users/index.html')

#🌟INICIO DE SESION

def inicio_sesion(request):

    if request.method == 'GET':

        return render(request, 'users/login.html')
    
    elif request.method == 'POST':

        correo = request.POST['nombre_usuario']
        clave = request.POST['clave']

        iniciar_sesion = Usuario.objects.filter(correo=correo, clave=clave)

        if iniciar_sesion:

            print("🌟Iniciando sesion...")
            print("🥳Inicio de sesion exitoso!")
            return redirect('Inicio')
        
    return render(request, 'users/login.html')

#🌟PAGINA INICIO

def Inicio(request):

    return render(request, 'users/agenda.html')