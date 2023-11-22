$(document).ready(function(){
    $("#formModificarP").submit(function(e){
        

       
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

        

        //valida la clave confirmadaP
        if (con_clave_modiP.trim() != con_clave_modiP.trim()){
            msjMostrarModiP += "<br>-La clave confirmada no es la misma";
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