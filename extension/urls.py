from django.contrib import admin
from django.urls import path
from .views import Pantalla,formAgregarUP,eliminarclase,Comentarios,formcomentarios,AgregarPla,CambiRol,AgregarRP,CambiarRol,modiJuegos,MJuegos,Comentarios,ModificarJuegos,formAgregarMP,ModificarP,formAgregarM,formOlvidado,formSesion,Registrarse,formAgregarU,Administrador,RegistrarseP,Login,Modificar,Olvidado,VerPerfil,plantillaMenu,formAgregarJ

urlpatterns = [
    
    path('',Pantalla,name="Pantalla"),
    path('Registrarse',Registrarse,name="Registrarse"),
    path('formAgregarUP',formAgregarUP,name="formAgregarUP"),
    path('Administrador',Administrador,name="Administrador"),
    path('eliminarclase/<int:codigo>',eliminarclase,name="eliminarclase"),
    path('RegistrarseP',RegistrarseP,name="RegistrarseP"),
    path('Login',Login,name="Login"),
    path('Modificar',Modificar,name="Modificar"),
    path('Olvidado',Olvidado,name="Olvidado"),
    path('VerPerfil',VerPerfil,name="VerPerfil"),
    path('plantillaMenu',plantillaMenu,name="plantillaMenu"),
    path('formAgregarJ', formAgregarJ,name="formAgregarJ"),
    path('formAgregarU', formAgregarU,name="formAgregarU"),
    path('formSesion', formSesion,name="formSesion"),
    path('formOlvidado', formOlvidado,name="formOlvidado"),
    path('formAgregarM', formAgregarM,name="formAgregarM"),
    path('ModificarP/<int:codigo>', ModificarP,name="ModificarP"),
    path('formAgregarMP', formAgregarMP,name="formAgregarMP"),
    path('Comentarios/<int:codigo>', Comentarios,name="Comentarios"),
    path('MJuegos/<int:id>', MJuegos,name="MJuegos"),
    path('ModificarJuegos', ModificarJuegos,name="ModificarJuegos"),
    path('modiJuegos', modiJuegos,name="modiJuegos"),
    path('CambiarRol/<int:id>', CambiarRol,name="CambiarRol"),
    path('CambiRol', CambiRol,name="CambiRol"),
    path('AgregarRP', AgregarRP,name="AgregarRP"),
    path('AgregarPla/<int:codigo>', AgregarPla,name="AgregarPla"),
    path('formcomentarios/<int:codigo>', formcomentarios,name="formcomentarios"),
    
]