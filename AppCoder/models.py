from django.db import models

# Create your models here.

class Equipo(models.Model):
    nombre = models.CharField(max_length=100)
    teamplayer = models.ManyToManyField('Jugador', related_name='equipos')

    def __str__(self):
        return self.nombre
    
class Jugador(models.Model):
    nombre = models.CharField(max_length=100)
    pais = models.CharField(max_length=50)
    edad = models.PositiveIntegerField()
    

    def __str__(self):
        return self.nombre
    
class Torneo(models.Model):
    nombre = models.CharField(max_length=100)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    juego = models.CharField(max_length=100)
    equipos_participantes = models.ManyToManyField('Equipo', related_name='torneos')

    def __str__(self):
        return self.nombre
