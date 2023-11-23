from django.db import models

# Create your models here.

class pregunta(models.Model):
    id_pregunta = models.AutoField(primary_key = True, verbose_name='id pregunta')
    nombreP      = models.CharField(max_length=250, verbose_name='nombre pregunta')

    def __str__(self)-> str:
        return self.nombreP
    
class area_conocimiento(models.Model):
    id_area = models.AutoField(primary_key = True, verbose_name='id Area conocimiento')
    nombreA      = models.CharField(max_length=250, verbose_name='nombre Area conocimiento')

    def __str__(self)-> str:
        return self.nombreA

class nivel_academico(models.Model):
    id_nivel = models.AutoField(primary_key = True, verbose_name='id nivel academico')
    nombreN     = models.CharField(max_length=250, verbose_name='nombre nivel academico')

    def __str__(self)-> str:
        return self.nombreN
    
class rol(models.Model):
    id_rol = models.AutoField(primary_key = True, verbose_name='id rol')
    nombreR = models.CharField(max_length=30, verbose_name='nombre rol')

    def __str__(self) -> str:
        return self.nombreR
    
class usuario(models.Model):
    idUsuario = models.AutoField(primary_key = True, verbose_name='id de usuario')
    nombreU   = models.CharField(max_length=50, verbose_name='nombre usuario'  )
    apellido  = models.CharField(max_length=50, verbose_name='apellido usuario')
    correo    = models.EmailField(max_length=254, verbose_name='correo usuario' )
    clave     = models.CharField(max_length=20, verbose_name='clave usuario')
    fotoU     = models.ImageField(upload_to="Foto Perfil")
    fechaU    = models.DateField(verbose_name='Fecha nacimiento')
    documentacion = models.ImageField(upload_to="Foto Documentacion", blank=True, null=True )
    respuesta = models.CharField(max_length=250, verbose_name='respuesta usuario')
    area_id_area = models.ForeignKey(area_conocimiento,on_delete=models.CASCADE, blank=True, null=True)
    nivel_id_nivel = models.ForeignKey(nivel_academico,on_delete=models.CASCADE, blank=True, null=True )
    pregunta_id_pregunta = models.ForeignKey(pregunta,on_delete=models.CASCADE)
    rol_id_rol = models.ForeignKey(rol,on_delete=models.CASCADE)

    def __str__(self)-> str:
        return self.nombreU
     
class clase(models.Model):
    id_clase = models.AutoField(primary_key = True, verbose_name='id clase')
    nombreC      = models.CharField(max_length=250, verbose_name='nombre clase')
    fechaC    = models.DateField(verbose_name='Fecha clase')
    hora   = models.TextField(verbose_name='hora clase')
    usuario_id_usuario = models.ForeignKey(usuario,on_delete=models.CASCADE)
    area_id_area = models.ForeignKey(area_conocimiento,on_delete=models.CASCADE)
    
    def __str__(self)-> str:
        return self.nombreC
    

class comentario(models.Model):
    id_comentario     = models.AutoField(primary_key = True, verbose_name='id comentario')
    comentarios = models.CharField(max_length=254,verbose_name='comentario')
    nota = models.CharField(max_length=254,verbose_name='comentario')
    usuario_id_usuario = models.ForeignKey(usuario,on_delete=models.CASCADE)
    clase_id_clase = models.ForeignKey(clase,on_delete=models.CASCADE)

    def __str__(self)-> str:
        return self.comentarios
    


    


    

    