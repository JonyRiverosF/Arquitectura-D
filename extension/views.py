from django.shortcuts import render, redirect
from .models import pregunta, rol, usuario, area_conocimiento, comentario, nivel_academico, clase
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from django.contrib.auth import authenticate,login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

def Pantalla(request):
    
    return render(request,'extension/Pantalla.html')


def Comentarios(request):
    return render(request,'extension/Comentarios.html')


def ModificarJuegos(request):
    return render(request,'extension/ModificarJuegos.html')

def MJuegos(request,id):
    return render(request,'extension/MJuegos.html')

def modiJuegos(request):
    return redirect('ModificarJuegos')

def eliminarJuego(request):
    return redirect('ModificarJuegos')

def Registrarse(request):
    listaPreguntas = pregunta.objects.all()
    nivelAcademico = nivel_academico.objects.all()
    
    contexto = {
        "preguntas": listaPreguntas,
        "nivel" :nivelAcademico,
    }
    return render(request,'extension/Registrarse.html',contexto)

def CambiarRol(request):
    return render(request,'extension/CambiarRol.html')

def Administrador(request):
    return render(request,'extension/administrador.html')

def CambiRol(request):
    return redirect('Administrador')

def RegistrarseP(request):
    listaPreguntas = pregunta.objects.all()
    AreaConocimiento = area_conocimiento.objects.all()
    
    contexto = {
        "preguntas": listaPreguntas,
        "area" :AreaConocimiento
    }
    return render(request,'extension/RegistrarseP.html',contexto)

def Login(request):
    logout(request)
    return render(request,'extension/Login.html')

def Modificar(request):
    return render(request,'extension/Modificar.html')

def eliminarRol(request):
    return redirect('AgregarRP')

def eliminarPlata(request):
    return redirect('AgregarPla')

def AgregarRP(request):
    return render(request,'extension/AgregarRP.html')

def AgregarPla(request):
    return render(request,'extension/AgregarPla.html')

def FormAgregarR(request):
    return redirect('AgregarRP')

def FormAgregarP(request):
    return redirect('AgregarPla')

def ModificarP(request):
    return render(request,'extension/ModificarP.html')

def Olvidado(request):
    return render(request,'extension/olvidado.html')

def VerPerfil(request):
    return render(request,'extension/ver perfil.html')

def WebServices(request):
    return render(request,'extension/webServices.html')

def xbox(request):
  return render(request,'extension/Exclusivo Xbox/xbox.html')

def Play(request):
    return render(request,'extension/Exclusivo Play/playstation.html')

def Pc(request):
    return render(request,'extension/Exclusivo PC/pc.html')
 
def Nintendo(request):
    return render(request,'extension/Exclusivo Nintendo/nintendo.html')
    
def Batman(request):
    return render(request,'extension/Exclusivo Play/BATMAN_ARKHAM_KNIGHT.html')

def DeadR(request):
    return render(request,'extension/Exclusivo Xbox/deadrising.html')

def Animal(request):
    return render(request,'extension/Exclusivo Nintendo/ANIMAL CROSSING.html')
    

def BMesa(request):
    return render(request,'extension/Exclusivo PC/BLACK MESA.html')
   
def plantillaMenu(request,id):
    return render(request,'extension/plantillaMenu.html')
    
def formOlvidado(request):
    return redirect('Olvidado')

def Agregar(request):
    return render(request,'extension/AgregarJuego.html')

def formAgregarJ(request):
    return redirect ('ModificarJuegos')
    
def formAgregarM(request):
    return render(request,'extension/Login.html')

def formAgregarMP(request):
    return render(request,'extension/Login.html')

def formAgregarU(request):
    
    contexto = {}

    vNombreU = request.POST['nombre']
    contexto["nombre"]=vNombreU

    vApellidoU = request.POST['apellido']
    contexto["apellido"]=vApellidoU

    vClaveU = request.POST['password']
    contexto["password"]=vClaveU

    vCorreoU = request.POST['email']
    contexto["email"]=vCorreoU
    
    vPregunta=request.POST['pregunta']
    variable = pregunta.objects.all()
    contexto["preguntas"]=variable

    vRespuesta=request.POST['respuesta']
    contexto["respuesta"]=vRespuesta

    vNivelA=request.POST['nivel']
    variableA = nivel_academico.objects.all()
    contexto["nivel"]=variableA

    vFechaU = request.POST['fecha']
    contexto["fecha"]=vFechaU

    vFotoU = request.FILES['fotoU']

    vRol = 1 
    vRegistroRol = rol.objects.get(id_rol=vRol)

    valida = usuario.objects.all()
    for forcorreo in valida:
        if forcorreo.correo == vCorreoU:
             messages.error(request,"Correo ya existente")
             return render(request,'extension/Registrarse.html',contexto)

    vRegistroPregunta = pregunta.objects.get(id_pregunta = vPregunta)
    vRegistroNivel = nivel_academico.objects.get(id_nivel = vNivelA)
    usuario.objects.create(nombreU=vNombreU, apellido=vApellidoU, clave=vClaveU, correo=vCorreoU, 
                            nivel_id_nivel=vRegistroNivel, fechaU=vFechaU, fotoU=vFotoU, pregunta_id_pregunta=vRegistroPregunta, respuesta=vRespuesta, rol_id_rol=vRegistroRol) 
    
    user = User.objects.create_user(vCorreoU,vCorreoU, vClaveU)      
    return redirect('Login')

def formAgregarUP(request):
    contexto = {}

    vNombreU = request.POST['nombre']
    contexto["nombre"]=vNombreU

    vApellidoU = request.POST['apellido']
    contexto["apellido"]=vApellidoU

    vClaveU = request.POST['password']
    contexto["password"]=vClaveU

    vCorreoU = request.POST['email']
    contexto["email"]=vCorreoU
    
    vPregunta=request.POST['pregunta']
    variable = pregunta.objects.all()
    contexto["preguntas"]=variable

    vRespuesta=request.POST['respuesta']
    contexto["respuesta"]=vRespuesta

    vAreaC=request.POST['area']
    variableA = area_conocimiento.objects.all()
    contexto["area"]=variableA

    vFechaU = request.POST['fecha']
    contexto["fecha"]=vFechaU

    vFotoU = request.FILES['fotoU']

    vFotoD = request.FILES['fotoD']

    vRol = 3 
    vRegistroRol = rol.objects.get(id_rol=vRol)

    valida = usuario.objects.all()
    for forcorreo in valida:
        if forcorreo.correo == vCorreoU:
             messages.error(request,"Correo ya existente")
             return render(request,'extension/Registrarse.html',contexto)

    vRegistroPregunta = pregunta.objects.get(id_pregunta = vPregunta)
    vRegistroArea = area_conocimiento.objects.get(id_area = vAreaC)
    usuario.objects.create(nombreU=vNombreU, apellido=vApellidoU, clave=vClaveU, correo=vCorreoU, 
                            area_id_area=vRegistroArea, fechaU=vFechaU, fotoU=vFotoU, documentacion=vFotoD, pregunta_id_pregunta=vRegistroPregunta, respuesta=vRespuesta, rol_id_rol=vRegistroRol) 
    
    user = User.objects.create_user(vCorreoU,vCorreoU, vClaveU)  

    return redirect('Login')

def formSesion(request):
    try:
        vCorreo = request.POST['loginEmail']
        vClave = request.POST['loginPassword']
        vRol = 0
        vRun= 0
        registro = usuario.objects.all()

        
        for rol in registro:
            if rol.correo == vCorreo and rol.clave == vClave:

                    vRun = rol.idUsuario
                    vRol = rol.rol_id_rol.id_rol
        user1 = User.objects.get(username = vCorreo)
        print(user1.username)
        pass_valida = check_password(vClave,user1.password)

        if not pass_valida:
            messages.error(request,"El usuario o la contraseña son incorrectos")
            return redirect('Login')

        user = authenticate(username=vCorreo,password = vClave)

        print(user)
        if user is not None:
            if vRol == 1:
                login(request,user)
                return redirect('VerPerfil')
                

            if vRol == 2:
                login(request,user)
                return redirect('Administrador')

            if vRol == 3:
                login(request,user)
                return redirect('Pantalla') 

            if vRol == 0:
                messages.success(request, "Usuario no registrado")
                return redirect('Login')
    except User.DoesNotExist:
            messages.error(request,"El usuario no existe")
            return redirect('Login')
    except Exception as e:
        print(e)

def formComentarioBT(request):
    return redirect('Batman')

def VerComentarios(request,id):
    return render(request,'extension/VerComentarios.html')

def eliminarComentario(request,id):
    return redirect('Comentarios')
