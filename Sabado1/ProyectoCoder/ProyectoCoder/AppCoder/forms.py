from django import forms


class EquipoFormulario(forms.Form):
    nombre = forms.CharField(max_length=100)
    pais = forms.CharField(max_length=50)

    
class JugadorFormulario(forms.Form):
    nombre = forms.CharField(max_length=100)
    pais = forms.CharField(max_length=50)
    edad = forms.IntegerField()

    
class TorneoFormulario(forms.Form):
    nombre = forms.CharField(max_length=100)
    fecha_inicio = forms.DateField()
    fecha_fin = forms.DateField()
    
    