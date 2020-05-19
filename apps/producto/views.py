from django.shortcuts import render, redirect

from .forms import RegistrarProductoForm, ModificarProductoForm
from .models import Producto

def Registrar(request):
	if request.method == 'POST':
		form = RegistrarProductoForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('producto:listar')
	else:
		form = RegistrarProductoForm()
	return render(request,'registrar_producto.html',{'form': form})

def Modificar(request, producto_id):
	producto = Producto.objects.get(id=producto_id)
	form = ModificarProductoForm(instance=producto)
	if request.method == "POST":
		form = ModificarProductoForm(request.POST, instance=producto)
		if form.is_valid():
			producto = form.save(commit=False)
			producto.save()
			return redirect('producto:listar')
	return render(request, 'modificar_producto.html',{'form': form})

def Listar(request):
	productos = Producto.objects.all()
	return render(request, "listar_productos.html", {'productos':productos})