from django.shortcuts import render

from .forms import RegistrarDonacionForm

def Registrar(request):
	return render(request, "registrar_donacion.html")

def Listar(request):
	return render(request, "listar_donaciones.html")
