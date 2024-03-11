from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import *
# Create your views here.

def player(request):


    return render(request, "player.html")

def inicio(request):

    return render(request, "inicio.html")

def torneos(request):

    return render(request, "torneos.html")

def equipos(request):

    return render(request, "equipos.html")