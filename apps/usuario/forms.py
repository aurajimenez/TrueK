from django import forms

from .models import Usuario

class RegistrarUsuarioForm(forms.ModelForm):


	class Meta:
		model = Usuario
		fields = ('nombre', 'telefono', 'localizacion', 'email', 'foto',)