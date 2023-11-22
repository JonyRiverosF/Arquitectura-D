from django.urls import path
from gametopia1.views import lista_comentario,detalle_comentario
from gametopia1.viewsLogin import login

urlpatterns = [
    path('lista_comentario/', lista_comentario, name="lista_comentario"),
    path('detalle_comentario/<id>', detalle_comentario, name="detalle_comentario"),
    path('login', login, name="login"),
]