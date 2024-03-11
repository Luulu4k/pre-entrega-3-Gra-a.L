from django.urls import path
from AppCoder.views import *

urlpatterns = [
    path("player/", player, name="Player"),
    path("", inicio, name="home"),
    path("ver_torneos", torneos, name="torneos"),
    path("ver_equipos", equipos, name="Team"),
]