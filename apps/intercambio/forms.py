from django import forms

from .models import Intercambio

class RegistrarIntercambioForm(forms.ModelForm):


	class Meta:
		model = Intercambio
		fields = ('oferente', 'producto_del_oferente', 'producto_del_receptor', 'receptor', 'estado', 'fecha_solicitud_intercambio','fecha_aceptacion_intercambio',)