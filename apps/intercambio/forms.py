from django import forms

from .models import Intercambio

class RegistrarIntercambioForm(forms.ModelForm):

	def clean(self):
		cleaned_data = super().clean()
		oferente = cleaned_data.get("oferente")
		receptor = cleaned_data.get("receptor")
		producto_del_oferente = cleaned_data.get("producto_del_oferente")
		producto_del_receptor = cleaned_data.get("producto_del_receptor")

		if oferente == receptor:
			mensaje = "El oferente no puede ser el mismo receptor"
			self.add_error('oferente', mensaje)
			self.add_error('receptor', mensaje)

		if producto_del_oferente == producto_del_receptor:
			mensaje2 = "El producto de intercambio no puede ser el mismo"
			self.add_error('producto_del_receptor', mensaje2)


	class Meta:
		model = Intercambio
		fields = ('producto_del_oferente', 'producto_del_receptor', 'receptor', 'fecha_solicitud_intercambio',)


class ModificarIntercambioForm(forms.ModelForm):

	def clean(self):
		cleaned_data = super().clean()
		oferente = cleaned_data.get("oferente")
		receptor = cleaned_data.get("receptor")

		if oferente == receptor:
			mensaje = "El receptor no puede ser el mismo oferente"
			self.add_error('oferente', mensaje)
			self.add_error('receptor', mensaje)

	class Meta:
		model = Intercambio
		fields = ('producto_del_oferente', 'producto_del_receptor',)