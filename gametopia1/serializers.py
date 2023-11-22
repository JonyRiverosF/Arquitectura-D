from rest_framework import serializers
from extension.models import comentario,videojuego
class comentarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = comentario
        fields = ['id_comentario','comentarios','usuario_id_usuario','videojuego_id_videojuego']

class videojuegoSerializer(serializers.ModelSerializer):
    class Meta:
        model = videojuego
        fields = ['id_videojuego','nombreV','descripcion','trailer','link','plataforma_id']