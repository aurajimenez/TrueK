from django.shortcuts import render, redirect

from datetime import date, datetime

from .forms import RegistrarDonacionForm, ModificarDonacionForm
from .models import Donacion, Producto

def Registrar(request):
	if request.method == 'POST':
		form = RegistrarDonacionForm(request.POST)	
		if form.is_valid():
			donacion = form.save(commit=False)
			print(donacion.estado)
			donacion.estado = 'Donado'
			print(donacion.estado)
			donacion.save()

			return redirect('donacion:listar')
	else:
		form = RegistrarDonacionForm()
	return render(request, 'registrar_donacion.html', {'form': form})

def Modificar(request, donacion_id):
	donacion = Donacion.objects.get(id=donacion_id)
	form = ModificarDonacionForm(instance=donacion)
	if request.method == "POST":
		form = ModificarDonacionForm(request.POST, instance=donacion)
		if form.is_valid():
			donacion = form.save(commit=False)
			donacion.save()
			return redirect('donacion:listar')
	return render(request, 'modificar_donacion.html',{'form': form})


def Listar(request):
	donaciones = Donacion.objects.all()
	print(donaciones)
	return render(request, "listar_donaciones.html", {'donaciones':donaciones})
