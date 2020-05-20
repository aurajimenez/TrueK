from django import forms

from .models import Usuario

class RegistrarUsuarioForm(forms.ModelForm):
	telefono = forms.CharField(required=True)
	localizacion = forms.CharField(required=True)
	photo = forms.ImageField(required=False)

	username = forms.CharField(required=True)
	password = forms.CharField(required=True, widget=forms.PasswordInput)

	class Meta:
		model = Usuario
		fields = ('username', 'first_name', 'last_name', 'email', 'password', 'telefono','localizacion','photo',)

class ModificarUsuarioForm(forms.ModelForm):

	class Meta:
		model = Usuario
		fields = ('username', 'first_name', 'last_name', 'email', 'password', 'telefono','localizacion','photo',)

class LoginUsarioForm(forms.ModelForm):
	username = forms.CharField(widget=forms.TextInput)
	password = forms.CharField(widget=forms.TextInput)
