from django.shortcuts import render, redirect

from datetime import date, datetime

from .forms import RegistrarIntercambioForm, ModificarIntercambioForm
from .models import Intercambio

def Registrar(request):
	if request.method == 'POST':
		form = RegistrarIntercambioForm(request.POST)
		if form.is_valid():
			form.save()
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
