from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from apps.usuario.models import Usuario
from apps.producto.models import Producto
from apps.intercambio.models import Intercambio
from apps.donacion.models import Donacion

def Preguntas_Frecuentes(request):
    return render(request, "preguntas_frecuentes.html")

def Inicio(request):
    productos = Producto.objects.all().count()
    usuarios = Usuario.objects.all().count()
    numero_intercambios_iniciados = Intercambio.objects.all().count()
    numero_donaciones_iniciadas = Donacion.objects.all().count()
    numero_intercambios_rechazados = Intercambio.objects.filter(estado="Rechazado").count()
    numero_intercambios_aceptados = Intercambio.objects.filter(estado="Aceptado").count()

    contexto = {
    'productos': productos,
    'usuarios': usuarios,
    'numero_intercambios_iniciados': numero_intercambios_iniciados,
    'numero_donaciones_iniciadas': numero_donaciones_iniciadas,
    'numero_intercambios_rechazados': numero_intercambios_rechazados,
    'numero_intercambios_aceptados': numero_intercambios_aceptados,
    }
    return render(request, "inicio2.html", contexto)