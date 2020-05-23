from django import forms

from .models import Producto

class RegistrarProductoForm(forms.ModelForm):

	descripcion = forms.CharField(required=True, widget=forms.Textarea)

	class Meta:
		model = Producto
		fields = ('nombre', 'descripcion', 'foto', 'etiquetas',)

class ModificarProductoForm(forms.ModelForm):
	descripcion = forms.CharField(required=True, widget=forms.Textarea)

	class Meta:
		model = Producto
		fields = ('nombre', 'descripcion', 'foto', 'etiquetas',)