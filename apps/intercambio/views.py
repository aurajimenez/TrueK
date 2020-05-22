from django.shortcuts import render, redirect

from datetime import date, datetime

from .forms import RegistrarIntercambioForm, ModificarIntercambioForm
from .models import Intercambio, Producto

def Registrar(request):
	if request.method == 'POST':
		form = RegistrarIntercambioForm(request.POST)
		if form.is_valid():
			intercambio = form.save(commit=False)
			intercambio.estado = 'Iniciado'
			intercambio.save()
			return redirect('intercambio:listar')
	else:
		form = RegistrarIntercambioForm()
	return render(request, 'registrar_intercambio.html', {'form': form})

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


def Listar(request):
	intercambios = Intercambio.objects.all()
	return render(request, "listar_intercambios.html", {'intercambios':intercambios})

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

def Rechazar(request, intercambio_id):
	intercambio = Intercambio.objects.get(id=intercambio_id)
	if request.method == "GET":
		intercambio.estado = 'Rechazado'
		intercambio.fecha_aceptacion_intercambio = date.today()
		intercambio.save()
		print("El intercambio fue Rechazado")
	return render(request, "aceptar_intercambio.html", {'intercambio':intercambio})