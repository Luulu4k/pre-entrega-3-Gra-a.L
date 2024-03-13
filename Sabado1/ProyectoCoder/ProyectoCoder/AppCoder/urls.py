from django.urls import path
from AppCoder.views import *

urlpatterns = [
    path("player/", player, name="Player"),
    path("", inicio, name="home"),
    path("ver_torneos", torneos, name="torneos"),
    path("equipos", equipos, name="Team"),
    path("crear_equipos", crear_equipos, name= "Ver Equipos"),
    path("crear_jugador", crear_jugador),
    path("crear_torneo", crear_torneo),

    path("buscar_equipo/", buscar_equipo),
    path("resultados", resultados),
]