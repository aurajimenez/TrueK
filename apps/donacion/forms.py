from django import forms

from .models import Donacion, Usuario, Producto

import datetime

class RegistrarDonacionForm(forms.ModelForm):
	def __init__(self, usuario_actual, *args, **kwargs):
	    super(RegistrarDonacionForm, self).__init__(*args, **kwargs) # va de primera luego de def __init__
	    self.fields["objecto_servicio"].queryset = Producto.objects.filter(dueno=usuario_actual)
	    self.fields["receptor"].queryset = Usuario.objects.exclude(id=usuario_actual.id)

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
		fields = ('objecto_servicio', 'receptor',)

class ModificarDonacionForm(forms.ModelForm):

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
		fields = ('objecto_servicio', 'receptor',)