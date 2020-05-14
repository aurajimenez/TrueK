from django.shortcuts import render, redirect

from .forms import RegistrarProductoForm
from .models import Producto

def Registrar(request):
	if request.method == 'POST':
		form = RegistrarProductoForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('producto:listar')
	else:
		form = RegistrarProductoForm()
	return render(request,'registrar_producto.html',{'form': form})

def Listar(request):
	return render(request, "listar_donaciones.html", {'donaciones':donaciones})