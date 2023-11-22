from django.shortcuts import render, redirect
from .models import pregunta, rol, usuario, videojuego, comentario, plataforma
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from django.contrib.auth import authenticate,login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

def Pantalla(request,id):
    if id == 0:

        listaJ = videojuego.objects.get(id_videojuego = 63)
        listaT = videojuego.objects.get(id_videojuego = 76)

        listal = videojuego.objects.get(id_videojuego = 62)
        listap = videojuego.objects.get(id_videojuego = 74)

        listam = videojuego.objects.get(id_videojuego = 102)
        listan = videojuego.objects.get(id_videojuego = 101)

        listah = videojuego.objects.get(id_videojuego = 78)
        listag = videojuego.objects.get(id_videojuego = 68)

        contexto={
            
            "VideoJ":listaJ,
            "VideoT":listaT,

            "VideoL":listal,
            "VideoP":listap,

            "VideoM":listam,
            "VideoN":listan,

            "VideoH":listah,
            "VideoG":listag

        }
        return render(request,'extension/Pantalla.html',contexto)
    
    lista = usuario.objects.get(idUsuario=id)
    listaJ = videojuego.objects.get(id_videojuego = 63)
    listaT = videojuego.objects.get(id_videojuego = 76)

    listal = videojuego.objects.get(id_videojuego = 62)
    listap = videojuego.objects.get(id_videojuego = 74)

    listam = videojuego.objects.get(id_videojuego = 102)
    listan = videojuego.objects.get(id_videojuego = 101)

    listah = videojuego.objects.get(id_videojuego = 78)
    listag = videojuego.objects.get(id_videojuego = 68)

    contexto={
            
            "Panta": lista,

            "VideoJ":listaJ,
            "VideoT":listaT,

            "VideoL":listal,
            "VideoP":listap,

            "VideoM":listam,
            "VideoN":listan,

            "VideoH":listah,
            "VideoG":listag
    }
    return render(request,'extension/Pantalla.html',contexto)

@login_required (login_url= 'Login' )
def Comentarios(request):

    vCorreo = request.user.username
    vUser = usuario.objects.get(correo=vCorreo)
    vRun = vUser.idUsuario
    vIDR = vUser.rol_id_rol.id_rol
    if vIDR != 2:
        return redirect (f'VerPerfil/{vRun}')
    
    listaUsuarios = usuario.objects.all()
    listaComentarios = comentario.objects.all()

    contexto = {
    "usuarios": listaUsuarios,
    "comentarios": listaComentarios

    }
    return render(request,'extension/Comentarios.html',contexto)

@login_required (login_url= 'Login' )
def ModificarJuegos(request):

    vCorreo = request.user.username
    vUser = usuario.objects.get(correo=vCorreo)
    vRun = vUser.idUsuario
    vIDR = vUser.rol_id_rol.id_rol
    if vIDR != 2:
        return redirect (f'VerPerfil/{vRun}')
    
    lista = videojuego.objects.all()
    contexto = {
        "ModificarV": lista
    }
    return render(request,'extension/ModificarJuegos.html',contexto)

@login_required (login_url= 'Login' )
def MJuegos(request,id):

    vCorreo = request.user.username
    vUser = usuario.objects.get(correo=vCorreo)
    vRun = vUser.idUsuario
    vIDR = vUser.rol_id_rol.id_rol
    if vIDR != 2:
        return redirect (f'VerPerfil/{vRun}')
    
    PlataM = plataforma.objects.all()
    VideoM = videojuego.objects.get(id_videojuego = id)
    contexto = {
        "lista_plataformas": PlataM,
        "datos": VideoM
    }
    return render(request,'extension/MJuegos.html',contexto)

@login_required (login_url= 'Login' )
def modiJuegos(request):

    vCorreo = request.user.username
    vUser = usuario.objects.get(correo=vCorreo)
    vRun = vUser.idUsuario
    vIDR = vUser.rol_id_rol.id_rol
    if vIDR != 2:
        return redirect (f'VerPerfil/{vRun}')

    vFotoM = request.FILES.get('fotoMV' , '')
    vIDV = request.POST['idV']
    vNombreV = request.POST['nombreV']
    vDesc = request.POST['descripcion']
    vTrailerV = request.POST['trailer']
    vLinkV = request.POST['link']
    vPlataM = request.POST['plataformaM']
                  
    VideojuegoModi = videojuego.objects.get(id_videojuego = vIDV)
    VideojuegoModi.nombreV = vNombreV
    VideojuegoModi.descripcion = vDesc
    VideojuegoModi.trailer = vTrailerV
    VideojuegoModi.link = vLinkV

    registroPlataM = plataforma.objects.get(id_plataforma = vPlataM)
    VideojuegoModi.plataforma_id = registroPlataM

    if vFotoM!='':
        VideojuegoModi.foto=vFotoM

    VideojuegoModi.save()
    messages.success(request,"Juego modificado.")
    return redirect('ModificarJuegos')

@login_required (login_url= 'Login' )
def eliminarJuego(request,id):

    vCorreo = request.user.username
    vUser = usuario.objects.get(correo=vCorreo)
    vRun = vUser.idUsuario
    vIDR = vUser.rol_id_rol.id_rol
    if vIDR != 2:
        return redirect (f'VerPerfil/{vRun}')
    
    EliminarV = videojuego.objects.get(id_videojuego = id)
    EliminarV.delete()
    messages.success(request,"Juego eliminado.")
    return redirect('ModificarJuegos')

def Registrarse(request):
    listaPreguntas = pregunta.objects.all()
    
    contexto = {
        "preguntas": listaPreguntas
    }

    return render(request,'extension/Registrarse.html', contexto)

@login_required (login_url= 'Login' )
def CambiarRol(request,id):

    vCorreo = request.user.username
    vUser = usuario.objects.get(correo=vCorreo)
    vRun = vUser.idUsuario
    vIDR = vUser.rol_id_rol.id_rol
    if vIDR != 2:
        return redirect (f'VerPerfil/{vRun}')
    
    usuariosC = usuario.objects.get(idUsuario = id)
    rolesC = rol.objects.all()

    contexto={
        "usuarioCa": usuariosC,
        "RolesU": rolesC
    }
    return render(request,'extension/CambiarRol.html', contexto)

@login_required (login_url= 'Login' )
def Administrador(request):

    vCorreo = request.user.username
    vUser = usuario.objects.get(correo=vCorreo)
    vRun = vUser.idUsuario
    vIDR = vUser.rol_id_rol.id_rol
    if vIDR != 2:
        return redirect (f'VerPerfil/{vRun}')
    
    listaUsuarios = usuario.objects.all()
    listaRoles = rol.objects.all()

    contexto = {
        "usuarios": listaUsuarios,
        "Roles" : listaRoles
    }
    return render(request,'extension/administrador.html', contexto)

@login_required (login_url= 'Login' )
def CambiRol(request):

    vCorreo = request.user.username
    vUser = usuario.objects.get(correo=vCorreo)
    vRun = vUser.idUsuario
    vIDR = vUser.rol_id_rol.id_rol
    if vIDR != 2:
        return redirect (f'VerPerfil/{vRun}')
    
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

def Contacto(request,id):
    if id == 0:
        return render(request,'extension/Contacto.html')
    lista = usuario.objects.get(idUsuario=id)
    contexto = {
        "contac": lista
    }

    return render(request,'extension/Contacto.html',contexto)

def Login(request):
    logout(request)
    return render(request,'extension/Login.html')

def Modificar(request):
    return render(request,'extension/Modificar.html')

@login_required (login_url= 'Login' )
def eliminarRol(request,id):

    vCorreo = request.user.username
    vUser = usuario.objects.get(correo=vCorreo)
    vRun = vUser.idUsuario
    vIDR = vUser.rol_id_rol.id_rol
    if vIDR != 2:
        return redirect (f'VerPerfil/{vRun}')
    
    EliminarR = rol.objects.get(id_rol = id)
    EliminarR.delete()
    messages.success(request,"Rol eliminado.")
    return redirect('AgregarRP')

@login_required (login_url= 'Login' )
def eliminarPlata(request,id):

    vCorreo = request.user.username
    vUser = usuario.objects.get(correo=vCorreo)
    vRun = vUser.idUsuario
    vIDR = vUser.rol_id_rol.id_rol
    if vIDR != 2:
        return redirect (f'VerPerfil/{vRun}')
    
    EliminarP = plataforma.objects.get(id_plataforma = id)
    EliminarP.delete()
    messages.success(request,"Plataforma eliminada.")
    
    return redirect('AgregarPla')

@login_required (login_url= 'Login' )
def AgregarRP(request):

    vCorreo = request.user.username
    vUser = usuario.objects.get(correo=vCorreo)
    vRun = vUser.idUsuario
    vIDR = vUser.rol_id_rol.id_rol
    if vIDR != 2:
        return redirect (f'VerPerfil/{vRun}')
    
    listaRols = rol.objects.all()
    
    contexto={
        "Roles" : listaRols
        
    }
    return render(request,'extension/AgregarRP.html',contexto)

@login_required (login_url= 'Login' )
def AgregarPla(request):

    vCorreo = request.user.username
    vUser = usuario.objects.get(correo=vCorreo)
    vRun = vUser.idUsuario
    vIDR = vUser.rol_id_rol.id_rol
    if vIDR != 2:
        return redirect (f'VerPerfil/{vRun}')
    
    listaPlat = plataforma.objects.all()
    
    contexto={
        "Plataforma" : listaPlat
    }
    return render(request,'extension/AgregarPla.html',contexto)

def FormAgregarR(request):

    vRolN = request.POST['RolName']
    rol.objects.create( nombreR=vRolN )
    messages.success(request,"Rol agregado.")

    return redirect('AgregarRP')

def FormAgregarP(request):

    vPlata = request.POST['PlataformaName']
    plataforma.objects.create( nombrePLA=vPlata )
    messages.success(request,"Plataforma agregada.")
    

    return redirect('AgregarPla')

def ModificarP(request,id):

    lista = usuario.objects.get(idUsuario=id)
    contexto={
        "ModificarP":lista
    }

    return render(request,'extension/ModificarP.html',contexto)

def Olvidado(request):
    
    listaPreguntas = pregunta.objects.all()
    contexto = {
        "preguntas": listaPreguntas
    }
    return render(request,'extension/olvidado.html', contexto)

@login_required (login_url= 'Login' )
def VerPerfil(request,id):

    lista = usuario.objects.get(idUsuario=id)
    contexto = {
        "usuarios": lista
    }

    return render(request,'extension/ver perfil.html', contexto)

def WebServices(request):
    return render(request,'extension/webServices.html')

def xbox(request,id):
    if id == 0:
        listaJuegos = videojuego.objects.filter(plataforma_id = 1)
        contexto = {
            "juegos": listaJuegos
        }
        return render(request,'extension/Exclusivo Xbox/xbox.html',contexto)
    
    lista = usuario.objects.get(idUsuario=id)
    listaJuegos = videojuego.objects.filter(plataforma_id = 1)
    contexto = {
        "xbo": lista,
        "juegos": listaJuegos
    }
    return render(request,'extension/Exclusivo Xbox/xbox.html', contexto)

def Play(request,id):
    if id == 0:
        listaJuegos = videojuego.objects.filter(plataforma_id = 3)
        contexto = {
            "juegos1": listaJuegos
        }
        return render(request,'extension/Exclusivo Play/playstation.html',contexto)

    lista = usuario.objects.get(idUsuario=id)
    listaJuegos = videojuego.objects.filter(plataforma_id = 3)
    contexto = {
        "Pla": lista,
        "juegos1": listaJuegos
    }
    return render(request,'extension/Exclusivo Play/playstation.html', contexto)

def Pc(request,id):
    if id == 0:
        listaJuegos = videojuego.objects.filter(plataforma_id = 4)
        contexto = {
            "juegos2": listaJuegos
        }
        return render(request,'extension/Exclusivo PC/pc.html',contexto)
    
    lista = usuario.objects.get(idUsuario=id)
    listaJuegos = videojuego.objects.filter(plataforma_id = 4)
    contexto = {
        "PC": lista,
        "juegos2": listaJuegos
    }
    return render(request,'extension/Exclusivo PC/pc.html',contexto)

def Nintendo(request, id):
    if id == 0:
        listaJuegos = videojuego.objects.filter(plataforma_id = 2)
        contexto = {
            "juegos3": listaJuegos
        }
        return render(request,'extension/Exclusivo Nintendo/nintendo.html',contexto)
    lista = usuario.objects.get(idUsuario=id)
    listaJuegos = videojuego.objects.filter(plataforma_id = 2)
    contexto = {
        "Nin": lista,
        "juegos3": listaJuegos
    }

    return render(request,'extension/Exclusivo Nintendo/nintendo.html',contexto)

def Batman(request, id):
    if request.user.is_authenticated:
        vCorreo = request.user.username
        vUser = usuario.objects.get(correo=vCorreo)
        vID = vUser.idUsuario

        juego = videojuego.objects.get(id_videojuego = id)
        Vcomen= comentario.objects.filter(videojuego_id_videojuego=id)
        contexto = {
            "ID" : vID,
            "videojuego1": juego,
            "Comentario" : Vcomen
        }
        return render(request,'extension/Exclusivo Play/BATMAN_ARKHAM_KNIGHT.html', contexto)
    else:

        juego = videojuego.objects.get(id_videojuego = id)
        Vcomen= comentario.objects.filter(videojuego_id_videojuego=id)
        contexto = {
            "videojuego1" : juego,
            "Comentario" : Vcomen
        }
        return render(request,'extension/Exclusivo Play/BATMAN_ARKHAM_KNIGHT.html', contexto)

def DeadR(request, id):
    if request.user.is_authenticated:
        vCorreo = request.user.username
        vUser = usuario.objects.get(correo=vCorreo)
        vID = vUser.idUsuario
        
        juego = videojuego.objects.get(id_videojuego = id)
        Vcomen= comentario.objects.filter(videojuego_id_videojuego=id)
        contexto = {
            "ID" : vID,
            "videojuego": juego,
            "comenT" : Vcomen
        }
        return render(request,'extension/Exclusivo Xbox/deadrising.html', contexto)
    
    else:
        juego = videojuego.objects.get(id_videojuego = id)
        Vcomen= comentario.objects.filter(videojuego_id_videojuego=id)
        contexto = {
            "videojuego": juego,
            "comenT" : Vcomen
        }
        return render(request,'extension/Exclusivo Xbox/deadrising.html', contexto)

def Animal(request, id):
    if request.user.is_authenticated:
        vCorreo = request.user.username
        vUser = usuario.objects.get(correo=vCorreo)
        vID = vUser.idUsuario
        
        juego = videojuego.objects.get(id_videojuego = id)
        Vcomen= comentario.objects.filter(videojuego_id_videojuego=id)
        contexto = {
            "ID" : vID,
            "videojuego3": juego,
            "Comentario" : Vcomen
        }
        return render(request,'extension/Exclusivo Nintendo/ANIMAL CROSSING.html', contexto)
    
    else:
        juego = videojuego.objects.get(id_videojuego = id)
        Vcomen= comentario.objects.filter(videojuego_id_videojuego=id)
        contexto = {
            "Comentario" : Vcomen,
            "videojuego3": juego
        }
        return render(request,'extension/Exclusivo Nintendo/ANIMAL CROSSING.html', contexto)
    
def BMesa(request, id):
    if request.user.is_authenticated:
        vCorreo = request.user.username
        vUser = usuario.objects.get(correo=vCorreo)
        vID = vUser.idUsuario
        
        juego = videojuego.objects.get(id_videojuego = id)
        Vcomen= comentario.objects.filter(videojuego_id_videojuego=id)
        contexto = {
            "ID" : vID,
            "videojuego2": juego,
            "Comentario" : Vcomen
        }
        return render(request,'extension/Exclusivo PC/BLACK MESA.html', contexto)
    
    else:
        juego = videojuego.objects.get(id_videojuego = id)
        Vcomen= comentario.objects.filter(videojuego_id_videojuego=id)
        contexto = {
            "videojuego2": juego,
            "Comentario" : Vcomen
        }
        return render(request,'extension/Exclusivo PC/BLACK MESA.html', contexto)

@login_required (login_url= 'Login' )    
def plantillaMenu(request,id):

    vCorreo = request.user.username
    vUser = usuario.objects.get(correo=vCorreo)
    vRun = vUser.idUsuario
    vIDR = vUser.rol_id_rol.id_rol
    if vIDR != 2:
        return redirect (f'VerPerfil/{vRun}')
    
    lista = usuario.objects.get(idUsuario=id)
    contexto ={
        "usuarios":lista

    }
    return render(request,'extension/plantillaMenu.html',contexto)

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
            return render(request,'extension/Modificar.html',contexto)
        else: 
            return redirect('Login')
    except usuario.DoesNotExist:
        messages.error(request, "No hay coincidencias ")
        return redirect('Olvidado')

@login_required (login_url= 'Login' )    
def Agregar(request):

    vCorreo = request.user.username
    vUser = usuario.objects.get(correo=vCorreo)
    vRun = vUser.idUsuario
    vIDR = vUser.rol_id_rol.id_rol
    if vIDR != 2:
        return redirect (f'VerPerfil/{vRun}')
    
    listaPlataforma = plataforma.objects.all()
    contexto = {
        "Plataformas": listaPlataforma
    }
    return render(request,'extension/AgregarJuego.html', contexto)

def formAgregarJ(request):
    
    vNombreJ = request.POST['NombreJ']
    vDescripcion = request.POST['DescripcionJ']
    vTrailer     = request.POST['TrailerJ']
    vFotoJ       = request.FILES['SeleccioneJ']
    vLink        = request.POST['LinkJ']
    vPlataforma  = request.POST['plataforma']

    vRegistroPlataforma = plataforma.objects.get(id_plataforma=vPlataforma)
    videojuego.objects.create( nombreV=vNombreJ, descripcion=vDescripcion,  
                              trailer=vTrailer, foto=vFotoJ,link=vLink , plataforma_id=vRegistroPlataforma)
    
    if vRegistroPlataforma.id_plataforma==4:
        return redirect ('ModificarJuegos' )
    if vRegistroPlataforma.id_plataforma==1:
        return redirect ('ModificarJuegos')
    if vRegistroPlataforma.id_plataforma==3:
        return redirect ('ModificarJuegos ')
    if vRegistroPlataforma.id_plataforma==2:
        return redirect ('ModificarJuegos')
    
def formAgregarM(request):
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

def formAgregarMP(request):

    vNombre = request.POST['nombreM']
    vApellido = request.POST['apellidoM']
    vTelefono =request.POST['telefonoM']
    vCorreo = request.POST['emailM']
    vFotoM = request.FILES.get('fotoMP', '')
    
    listaM = usuario.objects.get(correo=vCorreo) 

    if vNombre !='':
        listaM.nombreU=vNombre
    
    if vApellido !='':
        listaM.apellido=vApellido
    
    if vTelefono !='':
        listaM.telefono=vTelefono

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

    vTelefonoU = request.POST['telefono']
    contexto["telefono"]=vTelefonoU

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
    usuario.objects.create(nombreU=vNombreU, apellido=vApellidoU, clave=vClaveU, correo=vCorreoU, 
                            telefono=vTelefonoU, fechaU=vFechaU, fotoU=vFotoU, pregunta_id_pregunta=vRegistroPregunta, respuesta=vRespuesta, rol_id_rol=vRegistroRol) 
    
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
                return redirect(f'VerPerfil/{vRun}')
                

            if vRol == 2:
                login(request,user)
                return redirect('Administrador') 

            if vRol == 0:
                messages.success(request, "Usuario no registrado")
                return redirect('Login')
    except User.DoesNotExist:
            messages.error(request,"El usuario no existe")
            return redirect('Login')
    except Exception as e:
        print(e)

def formComentario(request):
    vComentario =request.POST['ComentarioJ']
    vIDComen =request.POST['id_com']
    
    
    vCorreo = request.user.username
    vUser = usuario.objects.get(correo=vCorreo)
    vJuego = videojuego.objects.get(id_videojuego=vIDComen)
    comentario.objects.create( comentarios=vComentario, usuario_id_usuario=vUser, videojuego_id_videojuego=vJuego)
    messages.success(request,"comentario enviado")
    return redirect(f'DeadR/{vIDComen}')

def formComentarioA(request):
    vComentario =request.POST['ComentarioJ']
    vIDComen =request.POST['id_com']
    
    vCorreo = request.user.username
    vUser = usuario.objects.get(correo=vCorreo)
    vJuego = videojuego.objects.get(id_videojuego=vIDComen)
    comentario.objects.create(comentarios=vComentario, usuario_id_usuario=vUser, videojuego_id_videojuego=vJuego)

    messages.success(request,"comentario enviado")

    return redirect(f'Animal/{vIDComen}')

def formComentarioBL(request):
    vComentario =request.POST['ComentarioJ']
    vIDComen =request.POST['id_com']
    
    vCorreo = request.user.username
    vUser = usuario.objects.get(correo=vCorreo)
    vJuego = videojuego.objects.get(id_videojuego=vIDComen)
    comentario.objects.create(comentarios=vComentario, usuario_id_usuario=vUser, videojuego_id_videojuego=vJuego)
    messages.success(request,"comentario enviado")
    return redirect(f'BMesa/{vIDComen}')

def formComentarioBT(request):
    vComentario =request.POST['ComentarioJ']
    vIDComen =request.POST['id_com']
    
    vCorreo = request.user.username
    vUser = usuario.objects.get(correo=vCorreo)
    vJuego = videojuego.objects.get(id_videojuego=vIDComen)
    comentario.objects.create(comentarios=vComentario, usuario_id_usuario=vUser, videojuego_id_videojuego=vJuego)
    messages.success(request,"comentario enviado")
    return redirect(f'Batman/{vIDComen}')

@login_required (login_url= 'Login' ) 
def VerComentarios(request,id):

    vCorreo = request.user.username
    vUser = usuario.objects.get(correo=vCorreo)
    vRun = vUser.idUsuario
    vIDR = vUser.rol_id_rol.id_rol
    if vIDR != 2:
        return redirect (f'VerPerfil/{vRun}')
    
    comen = comentario.objects.filter(usuario_id_usuario=id)

    contexto={
        "comenT": comen
    }
    return render(request,'extension/VerComentarios.html', contexto)

@login_required (login_url= 'Login' )  
def eliminarComentario(request,id):

    vCorreo = request.user.username
    vUser = usuario.objects.get(correo=vCorreo)
    vRun = vUser.idUsuario
    vIDR = vUser.rol_id_rol.id_rol
    if vIDR != 2:
        return redirect (f'VerPerfil/{vRun}')
    
    EliminarC = comentario.objects.get(id_comentario = id)
    EliminarC.delete()
    messages.success(request,"Comentario eliminado.")
    return redirect('Comentarios')
