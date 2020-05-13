from django.shortcuts import render, redirect

from .forms import RegistrarDonacionForm
from .models import Donacion

def Registrar(request):
	if request.method == 'POST':
		form = RegistrarDonacionForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('donacion:listar')
	else:
		form = RegistrarDonacionForm()
	return render(request, "registrar_donacion.html", {'form': form})


def Listar(request):
	donaciones = Donacion.objects.all()
	print(donaciones)
	return render(request, "listar_donaciones.html", {'donaciones':donaciones})
