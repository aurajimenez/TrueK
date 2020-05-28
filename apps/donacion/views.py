from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from datetime import date, datetime

from .forms import RegistrarDonacionForm, ModificarDonacionForm
from .models import Donacion, Producto

@login_required
def Registrar(request):
	
	if request.method == 'POST':
		form = RegistrarDonacionForm(request.user, request.POST)	
		if form.is_valid():
			usuario_actual = Donacion(donador = request.user)
			donacion = form.save(commit=False)
			donacion.donador = request.user
			donacion.estado = 'Iniciada'
			donacion.save()
			producto = donacion.objecto_servicio
			producto.estado = 'En proceso'
			producto.save()
			return redirect('donacion:listar')
	else:
		form = RegistrarDonacionForm(request.user)
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
	from django.db.models import FilteredRelation, Q
	donaciones = Donacion.objects.filter(Q(donador=request.user)|Q(receptor=request.user))
	return render(request, "listar_donaciones.html", {'donaciones':donaciones})

@login_required
def Aceptar(request, donacion_id):
	donacion = Donacion.objects.get(id=donacion_id)

	donacion.estado = 'Recibida'
	donacion.fecha_aceptacion = date.today()
	donacion.save()

	producto = donacion.objecto_servicio
	producto.estado = 'Donado'
	producto.dueno = request.user
	producto.save()
	return redirect('donacion:listar')

@login_required
def Rechazar(request, donacion_id):
	donacion = Donacion.objects.get(id=donacion_id)

	donacion.estado = 'Rechazada'
	donacion.fecha_aceptacion = date.today()
	donacion.save()

	producto = donacion.objecto_servicio
	producto.estado = 'Vigente'
	producto.save()
	return redirect('donacion:listar')
