from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view,permission_classes
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from .serializers import comentarioSerializer
from extension.models import comentario

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.

@csrf_exempt
@api_view(['GET','POST'])
@permission_classes((IsAuthenticated,))
def lista_comentario(request):
    if request.method == 'GET':
        Comentario =  comentario.objects.all()
        serializer = comentarioSerializer(Comentario, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = comentarioSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        

@api_view(['GET','PUT','DELETE'])
@permission_classes((IsAuthenticated,))
def detalle_comentario(request,id):
    try:
        Comentario =comentario.objects.get(id_comentario=id)
    except comentario.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = comentarioSerializer(Comentario)
        return Response(serializer.data)
    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer =comentarioSerializer(Comentario, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.erros , status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        Comentario.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    




    