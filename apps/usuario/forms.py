from django import forms

from .models import Usuario

class RegistrarUsuarioForm(forms.ModelForm):
	nombre = forms.CharField(required=True)
	telefono = forms.CharField(required=True)
	localizacion = forms.CharField(required=True)
	email = forms.EmailField(required=True)
	contrasena = forms.CharField(required=True)
	photo = forms.ImageField(required=False)

	class Meta:
		model = Usuario
		fields = ('nombre', 'telefono', 'localizacion', 'email', 'photo', 'contrasena',)

class ModificarUsuarioForm(forms.ModelForm):

	class Meta:
		model = Usuario
		fields = ('nombre', 'telefono', 'localizacion', 'email',)

class LoginUsarioForm(forms.ModelForm):

	class Meta:
		model = Usuario
		fields = ('email','contrasena',)