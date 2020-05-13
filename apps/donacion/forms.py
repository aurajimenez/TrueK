from django import forms

from .models import Donacion

class RegistrarDonacionForm(forms.ModelForm):


	class Meta:
		model = Donacion
		fields = ('donador', 'objecto_servicio', 'receptor', 'estado', 'fecha_donacion', 'fecha_aceptacion',)