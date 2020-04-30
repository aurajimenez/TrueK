from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.http import HttpResponse

from .models import Usuario
from .forms import RegistrarUsuarioForm

def Registrar(request):
	if request.method == 'POST':
		form = RegistrarUsuarioForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/usuario/listar/')
	else:
		form = RegistrarUsuarioForm()
	return render(request, "registrar_usuario.html", {'form': form})

def Listar(request):
	usuarios = Usuario.objects.all()
	return render(request, "listar_usuarios.html", {'usuarios':usuarios})