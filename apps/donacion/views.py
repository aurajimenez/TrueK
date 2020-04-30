from django.shortcuts import render

from .forms import RegistrarDonacionForm

def Registrar(request):
	if request.method == 'POST':
		form = RegistrarDonacionForm(request.POST)
		if form.is_valid():
			return HttpResponseRedirect('/donacion/listar/')
	else:
		form = RegistrarDonacionForm()
	return render(request, "registrar_donacion.html", {'form': form})


def Listar(request):
	return render(request, "listar_donaciones.html")
