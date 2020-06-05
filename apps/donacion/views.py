from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from datetime import date, datetime

from .forms import RegistrarDonacionForm, ModificarDonacionForm,RegistrarDonacionDesdeProductoForm
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
def RegistrarDesdeProducto(request, producto_id):
	producto = Producto.objects.get(id=producto_id)
	if request.method == 'POST':
		form = RegistrarDonacionDesdeProductoForm(request.user, producto, data=request.POST)	
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
		form = RegistrarDonacionDesdeProductoForm(request.user, producto)
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

@login_required
def Cancelar(request, donacion_id):
	donacion = Donacion.objects.get(id=donacion_id)
	producto = donacion.objecto_servicio
	producto.estado = 'Vigente'
	producto.save()
	donacion.delete()
	return redirect('donacion:listar')

@login_required
def Perfil(request, donacion_id):
    donacion = Donacion.objects.get(id=donacion_id)
    donador = donacion.donador
    receptor = donacion.receptor
    objecto_servicio = donacion.objecto_servicio
    estado = donacion.estado
    fecha_donacion = donacion.fecha_donacion
    fecha_aceptacion = donacion.fecha_aceptacion

    contexto = {
    'donacion':donacion,
    }
    return render(request, "perfil_donacion.html", {'donacion':donacion})