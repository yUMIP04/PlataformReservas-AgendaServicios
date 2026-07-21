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
            return redirect('inicio_sesion')
        
        else:
            print("❌ No se pudo registrar usuario.")
            return render(request, 'users/index.html')
        
    return render(request, 'users/index.html')

#🌟INICIO DE SESION

def inicio_sesion(request):

    if request.method == 'GET':

        return render(request, 'users/login.html')
    
    elif request.method == 'POST':

        correo = request.POST['correo_usuario']
        clave = request.POST['clave']

        try:
          
           usuario = Usuario.objects.get(correo=correo, clave=clave)
           request.session['usuario_rol'] = usuario.rol
           request.session['nombre_usuario'] = usuario.nombre

           if usuario.rol == "Profesional":
               
                print("🌟Iniciando sesion...")
                print("🥳Inicio de sesion exitoso!")
                return redirect('Inicio')

           elif usuario.rol == "Cliente":
               
                print("🌟Iniciando sesion...")
                print("🥳Inicio de sesion exitoso!")
                return redirect('catalogo')
        
        except Exception as e:

            print(f"Hubo un error al iniciar sesion: {e}")
            return render(request, 'users/login.html')

    return render(request, 'users/login.html')

#🌟 CERRAR SESION

def cerrar_sesion(request):

    request.session.flush()
    return redirect(request, 'inicio_sesion')