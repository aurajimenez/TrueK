from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from datetime import date, datetime

from .forms import RegistrarDonacionForm, ModificarDonacionForm
from .models import Donacion, Producto

@login_required
def Registrar(request):
	if request.method == 'POST':
		form = RegistrarDonacionForm(request.POST)	
		if form.is_valid():
			donacion = form.save(commit=False)
			donacion.estado = 'Donado'
			donacion.save()
			return redirect('donacion:listar')
	else:
		form = RegistrarDonacionForm()
	return render(request, 'registrar_donacion.html', {'form': form})

@login_required
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

@login_required
def Listar(request):
	donaciones = Donacion.objects.all()
	return render(request, "listar_donaciones.html", {'donaciones':donaciones})

@login_required
def Aceptar(request, donacion_id, producto_id):
	producto = Producto.objects.get(id=producto_id)
	donacion = Donacion.objects.get(id=donacion_id)
	if request.method == 'GET':
		donacion.estado = 'Recibida'
		donacion.fecha_aceptacion = date.today()
		
		donacion.save()
		producto.estado = 'Donado'
		producto.save()
		print("La donación fue aceptada")
		contexto = { 'donacion':donacion, 'producto':producto}
		#return redirect('donacion:listar')
		return render(request, "aceptar_donacion.html", contexto)
	return redirect('donacion:listar')

@login_required
def Rechazar(request, donacion_id):
	donacion = Donacion.objects.get(id=donacion_id)
	if request.method == 'GET':
		donacion.estado = 'Rechazada'
		donacion.fecha_aceptacion = date.today()
		donacion.save()
		print("La donación fue Rechazada")
	return render(request, "aceptar_donacion.html", {'donacion':donacion})
