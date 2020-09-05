from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import json as simplejson

from apps.usuario.models import Usuario
from apps.producto.models import Producto
from apps.intercambio.models import Intercambio
from apps.donacion.models import Donacion

def Preguntas_Frecuentes(request):
    return render(request, "preguntas_frecuentes.html")

def Inicio(request):
    productos = Producto.objects.all()
    numero_productos = productos.count()
    usuarios = Usuario.objects.all().count()
    numero_intercambios_iniciados = Intercambio.objects.all().count()
    numero_donaciones_iniciadas = Donacion.objects.all().count()
    numero_intercambios_rechazados = Intercambio.objects.filter(estado="Rechazado").count()
    numero_intercambios_aceptados = Intercambio.objects.filter(estado="Aceptado").count()

    contexto = {
    'productos': productos,
    'numero_productos': numero_productos,
    'usuarios': usuarios,
    'numero_intercambios_iniciados': numero_intercambios_iniciados,
    'numero_donaciones_iniciadas': numero_donaciones_iniciadas,
    'numero_intercambios_rechazados': numero_intercambios_rechazados,
    'numero_intercambios_aceptados': numero_intercambios_aceptados,
    }
    return render(request, "inicio2.html", contexto)

def pie_chart(request):
    labels = []
    data = []

    queryset = Usuario.objects.order_by('-first_name')[:5]
    for city in queryset:
        labels.append(city.first_name)
        data.append(city.first_name)

    return render(request, 'pie_chart.html', {
        'labels': labels,
        'data': data,
    })