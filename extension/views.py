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
    return render(request,'extension/Registrarse.html')

def CambiarRol(request):
    return render(request,'extension/CambiarRol.html')

def Administrador(request):
    return render(request,'extension/administrador.html')

def CambiRol(request):
    return redirect('Administrador')

def Contacto(request):
    return render(request,'extension/Contacto.html')

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
    return redirect('Registrarse')

def formSesion(request):
    return redirect('Login')

def formComentarioBT(request):
    return redirect(f'Batman/')

def VerComentarios(request,id):
    return render(request,'extension/VerComentarios.html')

def eliminarComentario(request,id):
    return redirect('Comentarios')
