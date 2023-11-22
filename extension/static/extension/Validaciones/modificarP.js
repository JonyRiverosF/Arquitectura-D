$(document).ready(function(){
    $("#formModificarP").submit(function(e){
        

        var nombre    = $("#nombreM").val();
        var apellido  = $("#apellidoM").val();
        var contacto  = $("#telefonoM").val();
        
        
        
        let msjMostrarModiP = "";
        let enviar = false;

        if(nombre.trim().length < 4 || nombre.trim().length > 50){
            msjMostrarModiP = msjMostrarModiP + "-El nombre debe tener entre 4 y 50 caracteres.";
            enviar = true;
            e.preventDefault();
        }

        var letra = nombre.trim().charAt(0);
        if(!esMayuscula(letra)){
            msjMostrarModiP += "<br>-El nombre debe comenzar con mayúscula.";
            enviar = true;
            e.preventDefault();
        }
    
        
        if(nombre.trim() == ""){
            msjMostrarModiP += "<br>-El campo nombre no puede estar vacío.";
            enviar = true;
            e.preventDefault();
        }

        if (nombre.match(/([0-9])/)){
            msjMostrarModiP += "<br>-Nombre inválido, no puede contener números.";
            enviar = true;
            e.preventDefault();
         }

        //Validar Apellido
        if(apellido.trim().length < 4 || apellido.trim().length > 50){
            msjMostrarModiP = msjMostrarModiP + "<br>-El apellido debe tener entre 4 y 50 caracteres.";
            enviar = true;
            e.preventDefault();
        }

        var letra = apellido.trim().charAt(0);
        if(!esMayuscula(letra)){
            msjMostrarModiP += "<br>-El apellido debe comenzar con mayúscula.";
            enviar = true;
            e.preventDefault();
        }


        if(apellido == ""){
            msjMostrarModiP += "<br>-El campo apellido no puede estar vacío.";
            enviar = true;
            e.preventDefault();
        }

        if (apellido.match(/([0-9])/)){
            msjMostrarModiP += "<br>-Apellido inválido, no puede contener números.";
            enviar = true;
            e.preventDefault();
         }

          //validar telefono


        if(contacto.trim() == ""){
            msjMostrarModiP += "<br>-El campo teléfono no puede estar vacío.";
            enviar = true;
            e.preventDefault();
        }
        
        if(contacto.trim().length < 9 || contacto.trim().length > 12){
            msjMostrarModiP += "<br>-El télefono son entre 9 y 11 números.";
            enviar = true;
            e.preventDefault();
        }

        if (contacto.match(/([a-z , A-Z])/)){
            msjMostrarModiP +="<br>-El campo télefono no permite letras.";
            enviar = true;
            e.preventDefault();
         }

        if (contacto.match(/([!,%,&,@,#,$,^,,?,_,~,.,])/)){
            msjMostrarModiP += "<br>-El teléfono no permite caracteres especiales";
            enviar = true;
            e.preventDefault();
         }
    




         


    


















        if(enviar){
            $("#mensaje_modificarP").html(msjMostrarModiP);
        }
        else{
            $("#mensaje_modificarP").html("-Perfil Modificado exitosamente.");
        }
    });




    $("#formModificar").submit(function(e){

        var clave_modiP     = $("#claveN").val();
        var con_clave_modiP = $("#claveCN").val();

        let msjMostrarModiP = "";
        let enviar = false;

       //validar passwordP

       if (con_clave_modiP.trim() != clave_modiP.trim()){
           msjMostrarModiP += "<br>-La clave confirmada no es la misma.";
           enviar = true;
           e.preventDefault();

       }

       if(clave_modiP.trim().length < 8 || clave_modiP.trim().length > 12){
           msjMostrarModiP = msjMostrarModiP + "<br>-Clave inválida debe tener entre 8 y 12 caracteres";
           enviar = true;
           e.preventDefault();
       }

       if(clave_modiP.trim()  == ""){
           msjMostrarModiP += "<br>-Clave inválida no puede estar vacío";
           enviar = true;
           e.preventDefault();
       }

       if (!clave_modiP.match(/([A-Z])/)){
           msjMostrarModiP += "<br>-Clave inválida Falta una letra mayúscula";
           enviar = true;
           e.preventDefault();
       }

       if (!clave_modiP.match(/([a-z])/)){
           msjMostrarModiP += "<br>-Clave inválida Falta una letra minúscula";
            enviar = true;
            e.preventDefault();
        }

        if (!clave_modiP.match(/([0-9])/)){
           msjMostrarModiP += "<br>-Clave inválida Debe contener al menos un numero";
           enviar = true;
           e.preventDefault();
        }

       if (!clave_modiP.match(/([!,%,&,@,#,$,^,,?,_,~,.])/)){
           msjMostrarModiP += "<br>-Clave inválida Debe contener un caracter especial  !,%,&,@,#,$,^,,?,_,~,.";
           enviar = true;
           e.preventDefault();
       }


       if(enviar){
        $("#mensaje_modificarP").html(msjMostrarModiP);
        }
        else{
        $("#mensaje_modificarP").html("-Perfil Modificado exitosamente.");
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