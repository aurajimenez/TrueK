from django import forms

from .models import Producto

class RegistrarProductoForm(forms.ModelForm):

	descripcion = forms.CharField(required=True, widget=forms.Textarea)



	class Meta:
		model = Producto
		fields = ('dueno', 'nombre', 'descripcion', 'foto', 'etiquetas', 'estado',)