from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.contrib import messages

from .models import Usuario
from .forms import RegistrarUsuarioForm, ModificarUsuarioForm

def Registrar(request):
	if request.method == 'POST':
		form = RegistrarUsuarioForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('usuario:listar')
	else:
		form = RegistrarUsuarioForm()
	return render(request, "registrar_usuario.html", {'form': form})

def Modificar(request, usuario_id):
	usuario = Usuario.objects.get(id=usuario_id)
	form = ModificarUsuarioForm(instance=usuario)
	if request.method == "POST":
		form = ModificarUsuarioForm(request.POST, instance=usuario)
		if form.is_valid():
			usuario = form.save(commit=False)
			form.save()
			return redirect('usuario:listar')
	return render(request, 'modificar_usuario.html',{'form': form})


def Listar(request):
	usuarios = Usuario.objects.all()
	return render(request, "listar_usuarios.html", {'usuarios':usuarios})


def Login(request):
	if request.method == 'POST':
		form = AuthenticationForm(request.POST)
		if form.is_valid():
			email = form.cleaned_data.get('email')
			contrasena = form.cleaned_data.get('contrasena')
			print(email)
			print(contrasena)
			user = authenticate(username=email, password=contrasena)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {email} ")
				return redirect('usuario:listar')
			else:
				messages.error(request, "Invalid username or password.")
		else:
			messages.error(request, "Invalid username or password.")
	form = AuthenticationForm()
	return render(request, "login.html", {'form': form})
