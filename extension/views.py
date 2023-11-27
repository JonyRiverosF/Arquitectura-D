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

def ModificarJuegos(request):
    return render(request,'extension/ModificarJuegos.html')

def MJuegos(request,id):
    claseM = clase.objects.get(id_clase = id)
    usuarioinicio= usuario.objects.get(correo = request.user.username)
    area=area_conocimiento.objects.all()
    contexto = {
        "datos": claseM,
        "usuario":usuarioinicio,
        "areas":area
    }
    return render(request,'extension/MJuegos.html',contexto)

def modiJuegos(request):
    
    vIDV = request.POST['idV']
    vNombreV = request.POST['nombreC']
    vDesc = request.POST['fechaC']
    vTrailerV = request.POST['hora']
    vPlataM = request.POST['plataformaM']
                  
    ClaseModi = clase.objects.get(id_clase = vIDV)
    ClaseModi.nombreC = vNombreV
    ClaseModi.fechaC = vDesc
    ClaseModi.hora = vTrailerV

    registroPlataM = area_conocimiento.objects.get(id_area = vPlataM)
    ClaseModi.area_id_area = registroPlataM

    ClaseModi.save()
    return redirect('VerPerfil')
    
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

def CambiarRol(request,id):

    usuariosC = usuario.objects.get(idUsuario = id)
    rolesC = rol.objects.all()

    contexto={
        "usuarioCa": usuariosC,
        "RolesU": rolesC
    }

    return render(request,'extension/CambiarRol.html',contexto)

def Administrador(request):
    listaUsuarios = usuario.objects.all()
    listaRoles = rol.objects.all()

    contexto = {
        "usuarios": listaUsuarios,
        "Roles" : listaRoles
    }

    return render(request,'extension/administrador.html',contexto)

def CambiRol(request):
    vID = request.POST['IDU']
    vCorreoC = request.POST['NombreUC']
    vRolC = request.POST['RolC']

    RolCambiar = usuario.objects.get(idUsuario = vID)
    RolCambiar.correo = vCorreoC
    
    registroRolC = rol.objects.get(id_rol = vRolC)
    RolCambiar.rol_id_rol = registroRolC

    RolCambiar.save()
    messages.success(request,"Rol modificado")

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
    usuarioinicio= usuario.objects.get(correo = request.user.username)
    area=area_conocimiento.objects.all()
    contexto = {
        "usuario":usuarioinicio,
        "areas":area
        
    }

    return render(request,'extension/Modificar.html',contexto)

def eliminarRol(request):
    return redirect('AgregarRP')

def eliminarPlata(request):
    return redirect('AgregarPla')

def AgregarRP(request):
    usuarioinicio= usuario.objects.get(correo = request.user.username)
    areas=area_conocimiento.objects.all()
    contexto={
        "areas": areas,
        "usuario":usuarioinicio
    }

    return render(request,'extension/AgregarRP.html', contexto)

def AgregarPla(request, codigo):
    area=area_conocimiento.objects.get(id_area=codigo)
    clases=clase.objects.filter(area_id_area=area)
    usuarioinicio= usuario.objects.get(correo = request.user.username)
    areas=area_conocimiento.objects.all()
    contexto={
        "clases": clases,
        "area":area,
        "areas": areas,
        "usuario":usuarioinicio
    }

    return render(request,'extension/AgregarPla.html',contexto)

def FormAgregarR(request):

    return redirect('AgregarRP')

def FormAgregarP(request):
    return redirect('AgregarPla')

def ModificarP(request ):
    return render(request,'extension/ModificarP.html')

def Olvidado(request):
    listaPreguntas = pregunta.objects.all()
    contexto = {
        "preguntas": listaPreguntas
    }
    return render(request,'extension/olvidado.html',contexto)

def VerPerfil(request):
     usuarioinicio=usuario.objects.get(correo=request.user.username)
     clases=clase.objects.filter(usuario_id_usuario=usuarioinicio.idUsuario)

     contexto = {
        "usuario": usuarioinicio,
        "clases":clases,
        
    }
     return render(request,'extension/ver perfil.html', contexto)

def eliminarclase(request, codigo):
    claseseleccionada=clase.objects.get(id_clase=codigo)
    claseseleccionada.delete()
    
    return redirect('VerPerfil')

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
    try: 
        vPregunta=request.POST['pregunta']
        vRespuesta=request.POST['respuestas']
        vCorreo=request.POST['emailO']
        vRegistroPregunta = pregunta.objects.get(id_pregunta = vPregunta)
        vVariable = usuario.objects.get(pregunta_id_pregunta=vRegistroPregunta, respuesta=vRespuesta,correo=vCorreo) 
    

        contexto ={ 
            "olvidado":vVariable

        }

        if vRespuesta==vVariable.respuesta:
            return render(request,'extension/ModificarJuegos.html',contexto)
        else: formAgregarMP
        return redirect('Login')
    except usuario.DoesNotExist:
        messages.error(request, "No hay coincidencias ")
        return redirect('Olvidado')

def Agregar(request):
    return render(request,'extension/AgregarJuego.html')

def formAgregarJ(request):
    vClaveN = request.POST['passwordN']
    vCorreo = request.POST['emailM']
    
    
    listaM = usuario.objects.get(correo=vCorreo) 


    if vClaveN !='':
        listaM.clave=vClaveN

    listaM.save()


    u = User.objects.get(username=vCorreo)
    u.set_password(vClaveN)
    u.save()

    contexto = {
        "modificarU": listaM
    }
    messages.success(request,"Usuario Modificado") 
    return render(request,'extension/Login.html',contexto)
       
def formAgregarM(request):
    usuarioinicio= usuario.objects.get(correo= request.user.username)
    titulo = request.POST['titulo']
    fecha = request.POST['fecha']
    hora = request.POST['hora']
    asignatura = request.POST['asignatura']

    asignaturas = area_conocimiento.objects.get(id_area=asignatura)
    clase.objects.create(
        
        nombreC=titulo,
        fechaC= fecha,
        hora=hora,
        usuario_id_usuario=usuarioinicio,
        area_id_area = asignaturas,
        
         
    )
    return redirect('VerPerfil')

def formAgregarMP(request):
    vNombre = request.POST['nombreM']
    vApellido = request.POST['apellidoM']
    vCorreo = request.POST['emailM']
    vFotoM = request.FILES.get('fotoMP', '')
    
    listaM = usuario.objects.get(correo=vCorreo) 

    if vNombre !='':
        listaM.nombreU=vNombre
    
    if vApellido !='':
        listaM.apellido=vApellido

    if vFotoM!='':
        listaM.fotoU=vFotoM

    listaM.save()

    u = User.objects.get(username=vCorreo)
    u.save()

    contexto = {
        "modificarU": listaM
    } 
    messages.success(request,"Usuario Modificado") 
    return render(request,'extension/Login.html',contexto)

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
                return redirect('VerPerfil') 

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

def Comentarios(request,codigo):
    usuarioinicio= usuario.objects.get(correo = request.user.username)
    area=area_conocimiento.objects.all()
    clases=clase.objects.get(id_clase=codigo)
    comen=comentario.objects.filter(clase_id_clase=clases)
    
    contexto={
        "comentarios":comen,
        "clases":clases,
        "usuario":usuarioinicio,
        "areas":area
    }

    return render(request,'extension/Comentarios.html',contexto)

def formcomentarios(request,codigo):
    usuarioinicio= usuario.objects.get(correo= request.user.username)
    clases=clase.objects.get(id_clase=codigo)
    comen = request.POST['comentario']
    nota = request.POST['nota']
    
    comentario.objects.create(
        
        comentarios=comen,
        nota= nota,
        usuario_id_usuario=usuarioinicio,
        clase_id_clase = clases,
        
         
    )
    return redirect('Comentarios',codigo)

def eliminarComentario(request,id):
    return redirect('Comentarios')
