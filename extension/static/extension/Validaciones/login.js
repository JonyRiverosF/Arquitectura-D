$(document).ready(function(){
    $("#formlogin").submit(function(e){
        

        var email_login    = $("#loginEmail").val();
        var password_login = $("#loginPassword").val();

        let msjMostrarLogin = "";
        let enviar = false;

        
        //valida email
        if((email_login).trim().indexOf('@', 0) == -1 || (email_login).trim().indexOf('.', 0) == -1) {
            msjMostrarLogin += "-El correo electrónico introducido es inválido. Debe contener un @";
            enviar = true;
            e.preventDefault();
        }
        if(email_login.trim() == ""){
            msjMostrarLogin += "<br>-El campo correo no puede estar vacío";
            enviar = true;
            e.preventDefault();
        }

         
        var emailRegex = /^[^\s@]+@[^\s@]+.[^\s@]+$/; 

        if (!emailRegex.test(email_login)) {
            msjMostrarLogin += "<br>-No debe comenzar con @";
            enviar = true;
            e.preventDefault();
        }
        
        //valida password
        if(password_login.trim().length < 8 || password_login.trim().length > 12){
            msjMostrarLogin = msjMostrarLogin + "<br>-Clave inválida debe tener entre 8 y 12 caracteres";
            enviar = true;
            e.preventDefault();
        }

        if(password_login.trim()  == ""){
            msjMostrarLogin += "<br>-Clave inválida no puede estar vacío";
            enviar = true;
            e.preventDefault();
        }

        if (!password_login.match(/([A-Z])/)){
           msjMostrarLogin += "<br>-Clave inválida Falta una letra mayúscula";
            enviar = true;
            e.preventDefault();
        }

        if (!password_login.match(/([a-z])/)){
            msjMostrarLogin += "<br>-Clave inválida Falta una letra minúscula";
             enviar = true;
             e.preventDefault();
         }

         if (!password_login.match(/([0-9])/)){
            msjMostrarLogin += "<br>-Clave inválida Debe contener al menos un número";
            enviar = true;
            e.preventDefault();
         }

        if (!password_login.match(/([!,%,&,@,#,$,^,,?,_,~,.=])/)){
            msjMostrarLogin += "<br>-Clave inválida Debe contener un caracter especial  !,%,&,@,#,$,^,,?,_,~,.,=";
            enviar = true;
            e.preventDefault();
         }












    

        if(enviar){
            $("#mensaje").html(msjMostrarLogin);
        }
        else{
            $("#mensaje").html("-Sesion Iniciada.");
        }

    });

    function esMayuscula(letra){
        console.log("Estoy aqui");
        console.log(letra);
        console.log(letra.toUpperCase());

        if(letra == letra.toUpperCase()){
            return true;
        }
        else{
            return false;
        }
    }
});
