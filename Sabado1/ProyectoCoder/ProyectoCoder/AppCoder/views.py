from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import Equipo, Jugador, Torneo
from AppCoder.forms import EquipoFormulario, JugadorFormulario, TorneoFormulario

# Create your views here.

def player(request):

    return render(request,"player.html")


def inicio(request):

    return render(request, "inicio.html")

def torneos(request):

    return render(request, "torneos.html")

def equipos(request):

    return render(request, "equipos.html")

#formularios
def crear_equipos(request):

    if request.method == "POST":

        formulario = EquipoFormulario(request.POST)
        
        if formulario.is_valid():

            info_dict = formulario.cleaned_data

            nuevo_equipo = Equipo (nombre = info_dict["nombre"],
                                   pais = info_dict["pais"])
            
            nuevo_equipo.save()

            return render(request, "inicio.html")
    
    else: 

        formulario = EquipoFormulario()

    return render(request, "crear_equipos.html", {"form":formulario})
                                  

def crear_jugador(request):

    if request.method == "POST":

        formulario = JugadorFormulario(request.POST)
        
        if formulario.is_valid():

            info_dict = formulario.cleaned_data

            nuevo_jugador = Jugador (nombre = info_dict["nombre"],
                                     pais = info_dict["pais"],
                                     edad = info_dict["edad"],)
            
            
            nuevo_jugador.save()

            return render(request, "inicio.html")
    
    else: 

        formulario = JugadorFormulario()

    return render(request, "crear_jugador.html", {"form":formulario})                


def crear_torneo(request):

    if request.method == "POST":

        formulario = TorneoFormulario(request.POST)
        
        if formulario.is_valid():

            info_dict = formulario.cleaned_data

            nuevo_torneo = Equipo (nombre = info_dict["nombre"],
                                   pais = info_dict["pais"])
            
            nuevo_torneo.save()
            
            
            return render(request, "inicio.html")
    
    else: 

        formulario = TorneoFormulario()

    return render(request, "crear_torneo.html", {"form":formulario})     



def buscar_equipo(request):

    return render(request,"buscar_equipo.html")
    
def resultados(request):

    equipo = request.GET["nombre_equipo"]

    resultados = Equipo.objects.filter(nombre_iexact=equipo)
    
    return render(request, "resultados.html", {"resultados":resultados})



