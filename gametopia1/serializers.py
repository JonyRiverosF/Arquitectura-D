from rest_framework import serializers
from extension.models import comentario
class comentarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = comentario
        fields = ['id_comentario','comentarios','usuario_id_usuario','videojuego_id_videojuego']

