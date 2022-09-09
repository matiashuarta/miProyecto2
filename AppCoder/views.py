from django.http import HttpResponse
from django.shortcuts import render
from AppCoder.models import *

# Create your views here.

def curso(request):

    materia = Curso(nombre="Diseño", camada=12345)

    materia.save()

    return HttpResponse(f"Estoy guardando el primer curso: {materia.nombre}")

def entregables(request):

    ente1 = Entregable(nombre="Examen 1", fechaEntrega="2022-09-08")

    ente1.save() #Guardar en la DB

    return HttpResponse(f"He guardado: {ente1.nombre} con fecha {ente1.fechaEntrega}")

