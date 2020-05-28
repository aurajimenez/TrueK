from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .forms import RegistrarProductoForm, ModificarProductoForm
from .models import Producto

@login_required
def Registrar(request):
	if request.method == 'POST':
		form = RegistrarProductoForm(request.POST, request.FILES)
		if form.is_valid():
			producto = form.save(commit=False)
			producto.dueno = request.user
			producto.save()
			return redirect('producto:listar')
	else:
		form = RegistrarProductoForm()
	return render(request,'registrar_producto.html',{'form': form})

@login_required
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

@login_required
def Listar(request):
	productos = Producto.objects.filter(dueno=request.user)
	return render(request, "listar_productos.html", {'productos':productos})


