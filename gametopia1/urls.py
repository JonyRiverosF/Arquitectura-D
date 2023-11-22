from django.urls import path
from gametopia1.views import lista_comentario,detalle_comentario,lista_videojuego,detalle_videojuego
from gametopia1.viewsLogin import login

urlpatterns = [
    path('lista_comentario/', lista_comentario, name="lista_comentario"),
    path('detalle_comentario/<id>', detalle_comentario, name="detalle_comentario"),
    path('lista_videojuego/', lista_videojuego, name="lista_videojuego"),
    path('detalle_videojuego/<id>', detalle_videojuego, name="detalle_videojuego"),
    path('login', login, name="login"),
]