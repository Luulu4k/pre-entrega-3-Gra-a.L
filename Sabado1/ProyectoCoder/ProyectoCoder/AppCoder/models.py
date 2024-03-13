from django.db import models

# Create your models here.

class Equipo(models.Model):
    nombre = models.CharField(max_length=100)
    pais = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre
    
class Jugador(models.Model):
    nombre = models.CharField(max_length=100)
    pais = models.CharField(max_length=50)
    edad = models.IntegerField()
    
    def __str__(self):
        return self.nombre
    
class Torneo(models.Model):
    nombre = models.CharField(max_length=100)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    
    
    def __str__(self):
        return self.nombre
