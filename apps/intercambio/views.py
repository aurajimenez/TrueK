from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from datetime import date, datetime

from .forms import RegistrarIntercambioForm, ModificarIntercambioForm
from .models import Intercambio, Producto

@login_required
def Registrar(request):
	if request.method == 'POST':
		form = RegistrarIntercambioForm(request.POST)
		if form.is_valid():
			intercambio = form.save(commit=False)
			intercambio.oferente = request.user
			intercambio.estado = 'Iniciado'
			intercambio.save()
			return redirect('intercambio:listar')
	else:
		form = RegistrarIntercambioForm()
	return render(request, 'registrar_intercambio.html', {'form': form})

@login_required
def Modificar(request, intercambio_id):
	donacion = Intercambio.objects.get(id=intercambio_id)
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
	intercambios = Intercambio.objects.all()
	return render(request, "listar_intercambios.html", {'intercambios':intercambios})

@login_required
def Aceptar(request, intercambio_id, producto_id):
	producto = Producto.objects.get(id=producto_id)
	intercambio = Intercambio.objects.get(id=intercambio_id)
	if request.method == "GET":
		intercambio.estado = 'Aceptado'
		intercambio.fecha_aceptacion_intercambio = date.today()
		intercambio.save()
		producto.estado = 'Intercambiado'
		producto.save()
		contexto = { 'intercambio':intercambio, 'producto':producto}
		print("El intercambio fue Aceptado")
	return render(request, "aceptar_intercambio.html", contexto)

@login_required
def Rechazar(request, intercambio_id):
	intercambio = Intercambio.objects.get(id=intercambio_id)
	if request.method == "GET":
		intercambio.estado = 'Rechazado'
		intercambio.fecha_aceptacion_intercambio = date.today()
		intercambio.save()
		print("El intercambio fue Rechazado")
	return render(request, "aceptar_intercambio.html", {'intercambio':intercambio})