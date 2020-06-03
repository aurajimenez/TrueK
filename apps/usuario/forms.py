from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import Usuario

class RegistrarUsuarioForm(UserCreationForm):

	email = forms.CharField(label="Correo electrónico")
	telefono = forms.CharField(label="Teléfono", required=True)
	localizacion = forms.CharField(label="Localización", required=True)

	class Meta:
		model = Usuario
		fields = ('username', 'first_name', 'last_name', 'email', 'telefono','localizacion', 'photo',)

class ModificarUsuarioForm(forms.ModelForm):
	photo = forms.ImageField(label="Foto", required=False)

	class Meta:
		model = Usuario
		fields = ('username', 'first_name', 'last_name', 'email', 'telefono','localizacion','photo',)

class LoginUsarioForm(forms.ModelForm):
	username = forms.CharField(widget=forms.TextInput)
	password = forms.CharField(widget=forms.TextInput)

class CambiarContrasenaForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput)

	class Meta:
		model = Usuario
		fields = ('password',)
