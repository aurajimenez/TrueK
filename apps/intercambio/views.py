from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from datetime import date, datetime

from .forms import RegistrarIntercambioForm, ModificarIntercambioForm, RegistrarIntercambioDesdeProductoForm
from .models import Intercambio, Producto

@login_required
def Registrar(request):
	
	if request.method == 'POST':
		form = RegistrarIntercambioForm(request.user, request.POST)
		if form.is_valid():
			usuario_actual = Intercambio(oferente = request.user)
			intercambio = form.save(commit=False)
			intercambio.oferente = request.user
			intercambio.receptor = intercambio.producto_del_oferente.dueno
			intercambio.receptor = intercambio.producto_del_receptor.dueno
			intercambio.estado = 'Iniciado'
			intercambio.save()

			producto_del_oferente = intercambio.producto_del_oferente
			producto_del_oferente.estado = 'En proceso'
			producto_del_oferente.save()
			return redirect('intercambio:listar')
	else:
		form = RegistrarIntercambioForm(request.user)
	return render(request, 'registrar_intercambio.html', {'form': form})

@login_required
def RegistrarDesdeProducto(request, producto_id):
	producto_del_receptor = Producto.objects.get(id=producto_id)	
	if request.method == 'POST':
		form = RegistrarIntercambioDesdeProductoForm(request.user, producto_del_receptor, data=request.POST)
		if form.is_valid():
			usuario_actual = Intercambio(oferente = request.user)
			intercambio = form.save(commit=False)
			intercambio.oferente = request.user
			intercambio.receptor = intercambio.producto_del_oferente.dueno
			intercambio.receptor = intercambio.producto_del_receptor.dueno
			intercambio.estado = 'Iniciado'
			intercambio.save()

			producto_del_oferente = intercambio.producto_del_oferente
			producto_del_oferente.estado = 'En proceso'
			producto_del_oferente.save()
			return redirect('intercambio:listar')
	else:
		form = RegistrarIntercambioDesdeProductoForm(request.user, producto_del_receptor)
	return render(request, 'registrar_intercambio.html', {'form': form})

@login_required
def Modificar(request, intercambio_id):
	intercambio = Intercambio.objects.get(id=intercambio_id)
	form = ModificarIntercambioForm(instance=intercambio)
	if request.method == "POST":
		form = ModificarIntercambioForm(request.POST, instance=intercambio)
		if form.is_valid():
			intercambio = form.save(commit=False)
			intercambio.save()
			return redirect('intercambio:listar')
	return render(request, 'modificar_intercambio.html',{'form': form})

@login_required
def Listar(request):
	from django.db.models import FilteredRelation, Q
	intercambios = Intercambio.objects.filter(Q(oferente=request.user)|Q(receptor=request.user))
	return render(request, "listar_intercambios.html", {'intercambios':intercambios})

@login_required
def Aceptar(request, intercambio_id):
	intercambio = Intercambio.objects.get(id=intercambio_id)
	intercambio.estado = 'Aceptado'
	intercambio.fecha_aceptacion_intercambio = date.today()
	intercambio.save()

	producto_del_oferente = intercambio.producto_del_oferente
	producto_del_oferente.estado = 'Intercambiado'
	producto_del_oferente.dueno = request.user
	producto_del_oferente.save()

	producto_del_receptor = intercambio.producto_del_receptor
	producto_del_receptor.estado = 'Intercambiado'
	producto_del_receptor.dueno = intercambio.oferente
	producto_del_receptor.save()

	contexto = { 'intercambio':intercambio, 'producto_del_oferente':producto_del_oferente, 'producto_del_receptor':producto_del_receptor }
	return redirect('intercambio:listar')

@login_required
def Rechazar(request, intercambio_id):
	intercambio = Intercambio.objects.get(id=intercambio_id)
	intercambio.estado = 'Rechazado'
	intercambio.fecha_aceptacion_intercambio = date.today()
	intercambio.save()
	producto_del_oferente = intercambio.producto_del_oferente
	producto_del_oferente.estado = 'Vigente'
	producto_del_oferente.save()
	return redirect('intercambio:listar')

@login_required
def Cancelar(request, intercambio_id):
	intercambio = Intercambio.objects.get(id=intercambio_id)
	producto_del_oferente = intercambio.producto_del_oferente
	producto_del_oferente.estado = 'Vigente'
	producto_del_oferente.save()
	intercambio.delete()
	return redirect('intercambio:listar')

@login_required
def Perfil(request, intercambio_id):
    intercambio = Intercambio.objects.get(id=intercambio_id)
    producto_del_oferente = intercambio.producto_del_oferente
    producto_del_receptor = intercambio.producto_del_receptor
    receptor = intercambio.receptor
    estado = intercambio.estado
    fecha_solicitud_intercambio = intercambio.fecha_solicitud_intercambio
    fecha_aceptacion_intercambio = intercambio.fecha_aceptacion_intercambio

    contexto = {
    'intercambio':intercambio,
    }

    return render(request, "perfil_intercambio.html", {'intercambio':intercambio})