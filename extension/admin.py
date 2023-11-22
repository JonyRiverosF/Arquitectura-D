from django.contrib import admin
from .models import usuario,comentario,rol,pregunta,clase,area_conocimiento,nivel_academico
# Register your models here.
admin.site.register(usuario)
admin.site.register(comentario)
admin.site.register(rol)
admin.site.register(pregunta)
admin.site.register(clase)
admin.site.register(area_conocimiento)
admin.site.register(nivel_academico)
