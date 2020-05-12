from django import forms

from .models import Donacion

class RegistrarDonacionForm(forms.ModelForm):
	donador = forms.CharField(required=True)
	objecto_servicio = forms.CharField(required=True)
	receptor = forms.CharField(required=True)
	estado = forms.CharField(required=False)
	fecha_donacion = forms.DateField(required=False)
	fecha_aceptacion = forms.DateField(required=False)


	class Meta:
		model = Donacion
		fields = ('donador', 'objecto_servicio', 'receptor', 'estado', 'fecha_donacion', 'fecha_aceptacion',)