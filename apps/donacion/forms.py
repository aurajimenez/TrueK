from django import forms

from .models import Donacion

class RegistrarDonacionForm(forms.ModelForm):

	def clean(self):
		cleaned_data = super().clean()
		donador = cleaned_data.get("donador")
		receptor = cleaned_data.get("receptor")

		if donador == receptor:
			mensaje = "El receptor no puede ser el mismo donador"
			self.add_error('donador', mensaje)
			self.add_error('receptor', mensaje)


	class Meta:
		model = Donacion
		fields = ('donador', 'objecto_servicio', 'receptor', 'estado', 'fecha_donacion', 'fecha_aceptacion',)