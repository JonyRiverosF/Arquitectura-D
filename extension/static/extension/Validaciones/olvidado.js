$(document).ready(function(){
    $("#formOlvidado").submit(function(e){
        

        var ComenJ = $("#ComeJ").val();

        let msjMostrarOlvidado = "";
        let enviar = false;

        


        if(enviar){
            $("#mensaje_Olvidado").html(msjMostrarOlvidado);
        }
        else{
            $("#mensaje_Olvidado").html("-En unos minutos le llegará el codigo.");
        }

        //Comentario Juegos

        var letra = ComenJ.trim().charAt(0);
        if(!esMayuscula(letra)){
            msjMostrarOlvidado += "<br>-El comentario debe comenzar con mayúscula";
            enviar = true;
            e.preventDefault();
        }

        if(ComenJ.trim() == ""){
            msjMostrarOlvidado += "<br>-No puede enviar un comentario vacío";
            enviar = true;
            e.preventDefault();
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