from django import forms

from .models import Intercambio, Producto, Usuario

class RegistrarIntercambioForm(forms.ModelForm):
	def __init__(self, oferente, *args, **kwargs):
		super(RegistrarIntercambioForm, self).__init__(*args, **kwargs)
		self.fields['producto_del_oferente'].queryset = Producto.objects.filter(dueno=oferente).exclude(estado='Donado').exclude(estado='Intercambiado').exclude(estado='En proceso')
		self.fields['producto_del_receptor'].queryset = Producto.objects.exclude(dueno=oferente).exclude(estado='Donado').exclude(estado='Intercambiado').exclude(estado='En proceso')

	def clean(self):
		cleaned_data = super().clean()
		producto_del_oferente = cleaned_data.get("producto_del_oferente")
		producto_del_receptor = cleaned_data.get("producto_del_receptor")


		if producto_del_oferente == producto_del_receptor:
			mensaje2 = "El producto de intercambio no puede ser el mismo"
			self.add_error('producto_del_receptor', mensaje2)


	class Meta:
		model = Intercambio
		fields = ('producto_del_oferente', 'producto_del_receptor',)

class RegistrarIntercambioDesdeProductoForm(forms.ModelForm):
	def __init__(self, oferente, producto_del_receptor, *args, **kwargs):
		super(RegistrarIntercambioDesdeProductoForm, self).__init__(*args, **kwargs)
		self.fields['producto_del_oferente'].queryset = Producto.objects.filter(dueno=oferente).exclude(estado='Donado').exclude(estado='Intercambiado').exclude(estado='En proceso')
		self.fields['producto_del_receptor'].queryset = Producto.objects.filter(id=producto_del_receptor.id)
		self.initial["producto_del_receptor"] = producto_del_receptor


	def clean(self):
		cleaned_data = super().clean()
		producto_del_oferente = cleaned_data.get("producto_del_oferente")
		producto_del_receptor = cleaned_data.get("producto_del_receptor")


		if producto_del_oferente == producto_del_receptor:
			mensaje2 = "El producto de intercambio no puede ser el mismo"
			self.add_error('producto_del_receptor', mensaje2)


	class Meta:
		model = Intercambio
		fields = ('producto_del_oferente', 'producto_del_receptor',)

class ModificarIntercambioForm(forms.ModelForm):

	class Meta:
		model = Intercambio
		fields = ('producto_del_oferente', 'producto_del_receptor',)