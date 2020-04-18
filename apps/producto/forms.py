from django import forms

from .models import Producto

class RegistrarProductoForm(forms.ModelForm):


	class Meta:
		model = Producto
		fields = ('dueno', 'nombre', 'descripcion', 'foto', 'etiquetas', 'estado',)